[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/putra214/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/putra214/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Day — Tuesday 24 November 2026

One image that sums up the world's news of Tuesday 24 November 2026, for
make.fun's "Sum up 24 November's world news in one image" bounty.

## The image

A one-page newspaper front page, drawn entirely in code
(`generate_poster.py`, Python + Pillow): a masthead dated
**TUESDAY, 24 NOVEMBER 2026**, a strip of six big numbers from the day's
news (11 hurt in the Riyadh tower strike, Huawei guilty on 10 of 12
counts, the M5.6 Nepal quake, 259 Democrat House seats, 139 Indonesians
deported, 19 killed in the Sudan drone strike), three lead stories —
the Houthi drone strike on Riyadh's PIF Tower, the investigation of
Shanghai party chief Chen Jining, and Huawei's conviction in Brooklyn —
each with its own rich illustration, a dotted world map with numbered
pins ("WHERE IT HAPPENED") matching the leads and grid stories, a UTC
timeline of the day, six more main stories (Israel killing Hamas security
chief Abu Nahal, South Korea scrambling jets against Russian planes, the
Shenzhou-24 crew announcement, the RSF drone strike in Blue Nile,
Ukraine's self-defence claim over the Libya ship strike, the Cartagena
hostage siege), twenty-six briefs from across nine regions (including
the UK's Houthi sanctions, the deportation of 139 Indonesians from a
Pasay scam hub, the release of Pope Francis's private diary, and
Australia's online safety deal), and a DATE CHECK box listing the big
non-24-November stories that were deliberately left out. Story kickers
are coloured by region so the spread of the news is visible at a glance.

Every event in the main sections happened, or was first reported, on
24 November 2026. Stories first reported on 24 November are framed
honestly ("reported Tuesday", "US ready to slap tariffs", "final count
confirms") rather than presented as if they happened that day. Stories
from other days are not in the main sections: the DATE CHECK box lists
nine of them with their real dates — the Solomon–Australia treaty
signing (25 Nov), the Shenzhou-24 launch (25 Nov), Australia's online
safety law (25 Nov), the formal US tariff announcement (25 Nov), Jimmy
Gomez quitting Congress (23 Nov), the ICJ Rohingya ruling (19 Nov), the
Hormuz tanker incidents (16–22 Nov), the Merkury corvette attack
(22 Nov), and Huang's return to Nvidia (23 Nov) — so nothing is
presented as the day's news that was not.

## How it is built

- `generate_poster.py` draws `entry.png` (1024x1024, PNG) with flat
  vector-style art and real text, so every letter stays sharp.
- `main.py` (Python 3.13, standard library only) copies `entry.png` to the
  output directory. It runs with no network and writes the same bytes on
  every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, under 1 MiB
```
