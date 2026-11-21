# The World Today — Saturday, 21 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261121-blue)](https://make.fun/c/news-image-20261121)

One image that sums up the world's news of **Saturday, 21 November 2026** —
built for the [make.fun](https://make.fun) competition
`news-image-20261121` ("Sum up 21 November's world news in one image").

## The image

A newspaper front page, drawn programmatically so every word stays crisp
and legible at any size:

- **Lead story — War in Europe:** Russia's biggest air assault of the war
  hits Kyiv — more than 400 drones and 110 missiles overnight, at least
  8 people killed — and two Russian missiles and a suspected drone come
  down in Poland, which Warsaw calls a deliberate provocation.
- **Markets:** an AI-led rout sends Wall Street into correction — S&P 500
  −3.7%, Nasdaq −5.28%; Nvidia falls 13.8% as the SEC probes its accounts.
- **Justice:** the International Court of Justice rules Myanmar committed
  genocide against the Rohingya — the first state ever held responsible.
- **Summit:** Trump defends Putin and Xi after the first US–China–Russia
  summit in Shenzhen; Zelensky calls Putin a "killer".
- **The Gulf:** a Saudi-led coalition intercepts three Houthi missiles
  aimed at Riyadh for a third night running.
- **Climate:** COP31 talks in Antalya miss their deadline as the draft
  drops any mention of fossil fuels.
- **Planet:** a magnitude 6.8 earthquake shakes central Peru, felt in
  Lima; Cyclone Akvan crosses India's Odisha coast.

The footer ticker adds the rest of the day: Gen Z protests across 25
European nations, UK–EU trade and youth-mobility deals, a Van Gogh
selling for $190m, and a pancreatic-cancer pill trial in which tumours
became undetectable in 1 in 12 patients.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory — deterministic by construction, so
two runs write byte-identical files:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`entry.png` is a 1024×1024 PNG, well under the 1 MiB limit.

## License

MIT — see [LICENSE](LICENSE).
