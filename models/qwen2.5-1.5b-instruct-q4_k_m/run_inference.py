#!/usr/bin/env python3
"""Run Qwen2.5-1.5B-Instruct (GGUF) over data/prompts.jsonl and record predictions.

Deterministic: greedy decoding (temperature=0) with a fixed seed, so a given GGUF
blob plus prompt set always yields the same predictions.jsonl.

Usage:
    python scripts/run_inference.py --gguf model/qwen2.5-1.5b-instruct-q4_k_m.gguf \
        --prompts data/prompts.jsonl --out out/predictions.jsonl [--limit 5] [--max-tokens 256]
"""
import argparse
import hashlib
import json
import os
import sys
import time

DEFAULT_SYSTEM = "You are a helpful, precise assistant. Follow the user's format constraints exactly."


def sha256_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def first_existing(*candidates):
    for c in candidates:
        if os.path.exists(c):
            return c
    return candidates[0]


def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gguf", required=True)
    ap.add_argument("--prompts", default="data/prompts.jsonl")
    ap.add_argument("--out", default="out/predictions.jsonl")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=256)
    ap.add_argument("--n-ctx", type=int, default=2048)
    ap.add_argument("--threads", type=int, default=os.cpu_count() or 2)
    args = ap.parse_args()

    try:
        from llama_cpp import Llama
    except ImportError:
        sys.exit("llama-cpp-python is not installed: pip install -r requirements.txt")

    if not os.path.exists(args.gguf):
        sys.exit("GGUF not found: %s" % args.gguf)

    model_sha = sha256_file(args.gguf)
    print("model: %s" % args.gguf)
    print("sha256: %s" % model_sha)

    llm = Llama(
        model_path=args.gguf,
        n_ctx=args.n_ctx,
        n_threads=args.threads,
        seed=0,
        verbose=False,
    )

    items = read_jsonl(args.prompts)
    if args.limit:
        items = items[: args.limit]

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    started = time.time()

    with open(args.out, "w", encoding="utf-8") as out:
        for i, item in enumerate(items, 1):
            messages = [
                {"role": "system", "content": DEFAULT_SYSTEM},
                {"role": "user", "content": item["prompt"]},
            ]
            t0 = time.time()
            resp = llm.create_chat_completion(
                messages=messages,
                temperature=0.0,
                top_p=1.0,
                max_tokens=args.max_tokens,
                seed=0,
            )
            dt = time.time() - t0
            text = (resp["choices"][0]["message"]["content"] or "").strip()
            usage = resp.get("usage", {})
            row = {
                "id": item["id"],
                "category": item.get("category"),
                "prompt": item["prompt"],
                "response": text,
                "latency_s": round(dt, 2),
                "completion_tokens": usage.get("completion_tokens"),
                "prompt_tokens": usage.get("prompt_tokens"),
            }
            out.write(json.dumps(row, ensure_ascii=False) + "\n")
            out.flush()
            print("[%d/%d] %-9s %5.1fs  %s" % (i, len(items), item["id"], dt, text[:60].replace("\n", " ")))

    meta = {
        "model": os.path.basename(args.gguf),
        "model_sha256": model_sha,
        "quant": "Q4_K_M",
        "prompts_sha256": sha256_file(args.prompts),
        "n_items": len(items),
        "n_ctx": args.n_ctx,
        "max_tokens": args.max_tokens,
        "temperature": 0.0,
        "seed": 0,
        "threads": args.threads,
        "wall_s": round(time.time() - started, 2),
    }
    with open(os.path.join(os.path.dirname(os.path.abspath(args.out)), "run_meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
