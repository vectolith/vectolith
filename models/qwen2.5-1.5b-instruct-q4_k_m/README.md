# Qwen2.5-1.5B-Instruct Q4_K_M — eval kit

Reproducible evaluation of **Qwen2.5-1.5B-Instruct**, GGUF **Q4_K_M**, 986,048,768 bytes
(sha256 `1adf0b11065d8ad2e8123ea110d1ec956dab4ab038eab665614adba04b6c3370`).

The weights are not committed here. They live in the private Kaggle dataset:

```bash
kaggle datasets download -d vectolith/qwen2-5-1-5b-instruct-q4-k-m --unzip
```

Provenance: weights from `Qwen/Qwen2.5-1.5B-Instruct` (Apache-2.0, 32k context, ChatML);
GGUF build from `bartowski/Qwen2.5-1.5B-Instruct-GGUF`. This is the 986 MB Q4_K_M build —
the same quant and weights published in `Qwen/Qwen2.5-1.5B-Instruct-GGUF`, whose own Q4_K_M
file is 1065 MB because of a different tensor/embedding layout choice.

## Files

| Path | Purpose |
|---|---|
| `run_inference.py` | Greedy inference (temperature 0, seed 0, n_ctx 2048) over `prompts.jsonl` |
| `score.py` | Deterministic rubric scorer — no judge model, no API keys |
| `rubric.md` | Vectolith Rubric v1: 5 dimensions, 13 points, pass = 9 |
| `prompts.jsonl` | 13 items with machine-checkable expectations |

## Run

```bash
pip install -r requirements.txt
python run_inference.py --gguf qwen2.5-1.5b-instruct-q4_k_m.gguf --out out/predictions.jsonl
python score.py --out out        # writes out/scores.json + out/report.md
```

`run_inference.py` records the model and prompt-set SHA-256 in `out/run_meta.json`, so a
score is tied to an exact blob. `score.py` maps each check to a rubric dimension and
renormalises the weights over the dimensions an item actually exercises; format or
correctness at 0 is a hard fail regardless of total.

## Baseline

A hand-written answer key scores 100 / 100 with 100% pass — the checks are calibrated to the
rubric, not to the model. Model results should be reported as scores.json plus the git SHA of
the run, never as a single number without the blob hash.
