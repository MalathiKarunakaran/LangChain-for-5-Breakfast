# LangChain for 5 Breakfast Ideas

A minimal LangChain script that asks an OpenAI chat model for **exactly 5 healthy breakfast ideas** and prints only the text of the reply.

*Week 2 · Day 5 assignment — Social Eagle (learn. build. operate)*

## What it shows

- `llm.invoke()` returns an **`AIMessage` object**, not a string; the text lives in `reply.content`.
- A **pinned prompt** (exact count, definition of "healthy", numbered format, no preamble) gives a predictable shape of output.
- The **API key** is read from a local `.env` file and is never hard-coded or committed.

## Project structure

```
breakfast/
├── breakfast.py      # the script
├── .env.example      # template for your API key (safe to commit)
├── .env              # your real key (git-ignored, create it yourself)
└── .gitignore        # ignores venv/ and .env
```

## Requirements

- Python 3.10+
- An OpenAI API key with available credits

## Setup

```bash
git clone https://github.com/MalathiKarunakaran/LangChain-for-5-Breakfast.git
cd LangChain-for-5-Breakfast

python3 -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\Activate.ps1

pip install langchain langchain-openai python-dotenv
```

Create your `.env` from the template and add your key — **one line, no quotes**:

```bash
cp .env.example .env
```

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
```

## Run

```bash
python breakfast.py
```

Sample output:

```
1. Greek yogurt with mixed berries and chia seeds.
2. Overnight oats with almond milk and sliced banana.
3. Scrambled eggs with spinach and whole grain toast.
4. Quinoa porridge topped with nuts and fruit.
5. Smoothie with spinach, protein powder, and unsweetened almond milk.
```

## Observations

**Two runs, different lists.** Running the script twice gave 1 identical idea, 2 similar ones, and 2 different ones. That is the model's default sampling temperature (~1) at work.

**Getting the same five every time.** Setting `temperature=0` (and optionally `seed`) in `ChatOpenAI(...)` makes the output near-repeatable, but OpenAI does not guarantee bit-for-bit determinism. If identical output is a hard requirement, cache the result instead of calling the model each time.

**What counts as "healthy" — and which cuisine.** The prompt defines healthy (protein/fibre, whole grains or millets, little added sugar, not fried), so the model doesn't decide that on its own. It does *not* specify cuisine, which is why the ideas came out mostly Western. Adding "Indian breakfasts" to the prompt changes that — whatever you leave unsaid, the model fills in for you.

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `No valid OPENAI_API_KEY in .env` | `.env` missing, empty, or key on the wrong line | Put `OPENAI_API_KEY=sk-...` on a single line |
| `python-dotenv could not parse statement` | Unclosed quote or broken line in `.env` | Remove quotes; keep the key on one line |
| `401 Incorrect API key` | Placeholder key, stray characters, or revoked key | Check with `cut -c1-25 .env`; regenerate the key if needed |
| Script runs but prints nothing | `print(reply.content)` missing | Make sure the last line prints `reply.content` |

## Security

`.env` is listed in `.gitignore`. Always confirm with `git status` that `.env` is **not** staged before committing — a key pushed to a public repo is scraped within minutes. If that ever happens, revoke the key immediately at platform.openai.com.
