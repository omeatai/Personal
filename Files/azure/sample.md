[Back to Microsoft Learn | AZ-900: Azure Fundamentals ](../../../azure_ai.md)

# 01 — Intro to Futures

## Table of Contents

- [Introduction](#introduction)
- [Detailed tutorial](#detailed-tutorial)
  - [What this bootcamp covers](#what-this-bootcamp-covers)
  - [Why they day trade futures](#why-they-day-trade-futures)
  - [What a futures contract is](#what-a-futures-contract-is)
  - [Symbols, minis, and micros](#symbols-minis-and-micros)
  - [The continuous contract](#the-continuous-contract)
  - [Tick size and tick value](#tick-size-and-tick-value)
  - [How to read a contract code](#how-to-read-a-contract-code)
  - [When futures trade](#when-futures-trade)
  - [Gold as the session example](#gold-as-the-session-example)
  - [Prop firm or self-funded](#prop-firm-or-self-funded)
  - [What comes next](#what-comes-next)
- [Summary](#summary)
- [References](#references)

## Introduction

Video chapter 1 of the Peachy Investor Futures Bootcamp. The lesson is an overview: why this desk day trades futures instead of stocks or options, how contract codes and tick values work, which hours they actually trade, and the path from a free NinjaTrader paper trial into a prop firm. Strategy rules come in later days. Coach Carrie covers tick value and margin in the next episode.

## Detailed tutorial

**Peachy Investor education guide** · Raw transcript: [01-Intro to Futures.txt](../../Transcripts/transcripts-txt/01-Intro%20to%20Futures.txt)

<details id="what-this-bootcamp-covers">
<summary><strong>What this bootcamp covers</strong></summary>

This is day one of a 10-day futures bootcamp, built in 10 to 30 minute pieces so it can be finished around a full-time job. The path she lays out:

1. Learn the contracts, the hours, and a few strategies you can paper trade immediately.
2. Set up a two-week free NinjaTrader trial and paper trade with no capital at risk.
3. Day 9 is prop firms. Day 10 is a written trading plan and risk rules.
4. Coaches who have been with her for more than three years teach parts of it. Carrie (the captions also say Carey and Kerry) takes the next episode on tick value and margin. Goose trades the New York morning. Van trades the Asian session.

Paid members are told the trading school goes deeper than this video. Free viewers are told the bootcamp itself is the lesson, not a teaser.

Take notes. She tells you to pause.

</details>

<details id="why-they-day-trade-futures">
<summary><strong>Why they day trade futures</strong></summary>

The same comparison slide stays up for the first seven minutes. Read it against what she says, because the slide is the outline and the voiceover is the reason.

![00:08 — Futures 101 comparison of options and stocks versus futures](figures/00-08.jpg)

*Figure: 00:08. Futures 101 crash course. Options and stocks on the left, futures on the right.*

| Options and stocks | Futures, as this desk uses them |
| --- | --- |
| Theta and the other Greeks can drain an option while the stock goes sideways | No theta and no Greeks. A sideways market does not charge you for time |
| Less leverage | More leverage. A small account can control a large contract, and can also lose faster |
| Limited hours. Options, as of this recording, do not trade overnight | Nearly 23 hours a day. Premarket and the Asian session have tradable volume on many days, not only on news |
| Less premarket and after-hours volatility unless there is news | Premarket and after-hours volatility shows up most days of the week |
| Options add expiration and strike selection | Long means buy the contract. Short means sell the contract |

Two boundaries she states up front:

- This video is about **day trading**. Peachy Macro swing content is stocks and options. They do not swing trade futures.
- Futures are what she says people graduate to, and she calls them one of the harder products to learn. Leverage is the reason the later lessons lean on prop firms and micros instead of a large cash account.

Her starter sequence is paper trade on NinjaTrader first, because a prop-firm evaluation costs money. She treats the prop account as the next step after paper, not the first click. The "$100 into something like a $50,000 account" line is a preview of day 9, not a setup you copy from this episode.

</details>

<details id="what-a-futures-contract-is">
<summary><strong>What a futures contract is</strong></summary>

![07:55 — Investopedia futures definition and the four symbol boxes](figures/07-55.jpg)

*Figure: 07:55. The definition on the left, and the four products they actually trade on the right.*

A future is a derivative contract that obligates the parties to buy or sell an asset at a set date and price. She says the definition scares people because it sounds like you could be forced to take delivery (her example is oil arriving at your door). In practice she tells you not to manage that yourself:

- Trade the contract with the **highest volume**.
- When expiration gets close, volume **rolls** into the next month. That is the one you switch to. She says this often happens about a month out, and the broker usually blocks a contract that is about to expire.
- Or skip the month code entirely and chart the **continuous contract** (next section).

</details>

<details id="symbols-minis-and-micros">
<summary><strong>Symbols, minis, and micros</strong></summary>

The four boxes on that same slide are the products. A mini is the full-size contract they mean by "ES" or "NQ". A micro is the smaller contract with the same price, a fraction of the dollar risk.

| Mini | Micro | What it tracks | Stock she maps it to |
| --- | --- | --- | --- |
| /ES | /MES | S&P 500 | SPY |
| /NQ | /MNQ | Nasdaq-100 | QQQ |
| /CL | /MCL | Crude oil | — |
| /RTY | /M2K | Russell 2000 | IWM |

Gold is /GC, and the micro is /MGC. It is not in the four boxes, but she charts it later and calls it a premarket and Asian-session product.

Beginners execute the micro. Her shortcut is to put an **M** in front of the root: MES, MNQ, MGC, MCL.

</details>

<details id="the-continuous-contract">
<summary><strong>The continuous contract</strong></summary>

TradingView is the charting platform. A later day is the full TradingView tutorial. This pass is only the symbol trick.

![10:12 — TradingView symbol search on ES1!](figures/10-12.jpg)

*Figure: 10:12. Symbol search for `ES1!`, the continuous E-mini S&P 500. Pick the CME futures row, not the electricity contract that also starts with ES.*

Type the root plus `1!`. `ES1!` and `NQ1!` always follow the front contract, so you are not choosing `ESU26` by hand. She calls that the hack.

![10:50 — MGC1! five-minute micro gold](figures/10-50.jpg)

*Figure: 10:50. `MGC1!` on a 5-minute chart, the micro gold contract, during the Jul 16, 2026 morning session.*

![11:08 — Symbol search for MNQ](figures/11-08.jpg)

*Figure: 11:08. Searching `MNQ` returns Micro E-mini Nasdaq-100 futures. That is the execution symbol for a beginner who used to trade QQQ.*

![11:25 — QQQ five-minute chart, the stock version of NQ](figures/11-25.jpg)

*Figure: 11:25. QQQ on the 5-minute chart. She pulls it up to show the stock equivalent of NQ: same index, no tick-value math.*

</details>

<details id="tick-size-and-tick-value">
<summary><strong>Tick size and tick value</strong></summary>

A stock moving from 70 to 71 is one dollar per share. A future does not work that way. **Tick size** is the smallest price step. **Tick value** is how many dollars that step is worth for one contract. They are different for ES, NQ, and oil, which is why the same-looking move can be a very different profit and loss.

The captions say "1250" and "$1250". The slide, and her own arithmetic (four ticks equal $50), is **$12.50**.

![12:08 — Tick size and value table](figures/12-08.jpg)

*Figure: 12:08. Tick size is the minimum price step. Dollar value is per contract, per tick.*

| Contract | Tick size | Value of 1 tick |
| --- | --- | --- |
| E-mini S&P 500 (ES) | 0.25 points | $12.50 |
| Micro E-mini S&P (MES) | 0.25 points | $1.25 |
| Nasdaq E-mini (NQ) | 0.25 points | $5.00 |
| Crude oil (CL) | $0.01 per barrel | $10.00 |

MES at $1.25 per tick is one tenth of ES. That is the practical reason she wants beginners on micros: same chart, smaller dollars.

![12:55 — One ES tick and one ES point at 6,200](figures/12-55.jpg)

*Figure: 12:55. Buy one ES at 6,200.00. The next price, 6,200.25, is one tick.*

Worked example from the slide, one ES contract:

- 6,200.00 to 6,200.25 is **1 tick** = **$12.50**.
- 6,200.00 to 6,201.00 is **1.00 point**.
- One point is 4 ticks, because 0.25 × 4 = 1.
- 4 × $12.50 = **$50** per point on ES.

She says you do need this, and also says not to get stuck on it. Carrie repeats it with more chart examples on day two or day three.

</details>

<details id="how-to-read-a-contract-code">
<summary><strong>How to read a contract code</strong></summary>

If you are not on the continuous symbol, the listed contract looks like `ESU26`.

![14:05 — ESU26 broken into symbol, month, and year](figures/14-05.jpg)

*Figure: 14:05. Barchart-style rows for the September 2026 contracts, with `ESU26` split into ES, U, and 26.*

`ESU26` means:

- **ES** — the product (S&P 500 E-mini).
- **U** — the expiration month. U is September.
- **26** — the year, 2026.

The rows under it on this frame are `ETU26` (S&P 500 micro, Sep 2026) and `NQU26` (Nasdaq 100 E-mini, Sep 2026). She is recording in July 2026, so the nearby month codes she calls out are July **N**, August **Q**, September **U**, and October **V**. She does not want the July contract, because it is too close to expiration and the volume will already be leaving it.

![14:45 — CME month letters, cursor on September U](figures/14-45.jpg)

*Figure: 14:45. CME Group month codes. The cursor is on September = U.*

| Month | Code | Month | Code |
| --- | --- | --- | --- |
| January | F | July | N |
| February | G | August | Q |
| March | H | September | U |
| April | J | October | V |
| May | K | November | X |
| June | M | December | Z |

She still prefers not to pick these by hand. On TradingView, `NQ1!` (she says it as "NQ, one exclamation mark") is the continuous contract.

When you do need the listed month, for example inside NinjaTrader, she uses Barchart: Futures, then Indices (or Energies for oil, Metals for gold), then sort by volume. Trade the row with the most volume.

![16:00 — Barchart indices sorted with the volume column visible](figures/16-00.jpg)

*Figure: 16:00. Barchart indices on Thu, Jul 16, 2026. `NMU26` (Nasdaq 100 micro, Sep 2026) leads this frame at about 2.03 million volume. `ESU26` is the S&P 500 E-mini for September 2026.*

On this frame the September micro Nasdaq is the highest-volume index row, which is the same rule she states: follow the volume, and in July that volume is already in the September contract rather than July.

</details>

<details id="when-futures-trade">
<summary><strong>When futures trade</strong></summary>

All times below are Eastern.

![16:40 — Weekly schedule and the three session icons](figures/16-40.jpg)

*Figure: 16:40. Weekly hours at the top. The 9:30 icon is labeled "Pre-market" on the slide. She stops and corrects it: that icon is the cash open, not premarket.*

Weekly clock:

- Opens Sunday at 6:00 p.m.
- Trades nearly 24 hours.
- Daily maintenance halt from 5:00 p.m. to 6:00 p.m. She wants you flat about 15 minutes early, around 4:45 p.m.
- Week ends Friday at 5:00 p.m. Closed all Saturday. Reopens Sunday at 6:00 p.m.

![18:15 — Best times, including the lunch lull and the Asian session](figures/18-15.jpg)

*Figure: 18:15. The working hours. The slide says "market oepns at 9am". She means leave the premarket trade before the 9:30 open, around 9:00 to 9:15, because the open itself is chop.*

| Window (ET) | What she wants you to do |
| --- | --- |
| 6:00–7:00 a.m. | Premarket. Carrie's window. Volume is usually there. Stop around 9:00–9:15 a.m. |
| 9:30 a.m. | Cash open. Volatile and choppy. Let it settle. The 30-minute opening range ends near 10:00 a.m., and later days build order models around that. |
| 10:00 a.m.–12:00 p.m. | Cleaner trend. Goose's New York window. She calls 10:00 a.m. the best time if you want the open to finish chopping. |
| 12:00–1:00 p.m. | Lunch lull. Do not trade. Volume is poor and the strategies fail. |
| 1:00–2:00 p.m. into the close | Continuation trades often show up again. |
| 3:00–4:00 p.m. | Power hour. 4:00 p.m. is the official cash close. Futures themselves keep trading until the 5:00 p.m. halt. |
| 6:00–7:00 p.m. | Reopen. Moves here are usually small. |
| 8:00–9:00 p.m. | Asian session trend window. Hong Kong, China, and Singapore are opening. Van trades this from the West Coast. From the East Coast it is late unless you are a night owl. |

</details>

<details id="gold-as-the-session-example">
<summary><strong>Gold as the session example</strong></summary>

Indices in the early morning are "iffy". Gold is the product she uses when the trade is premarket, and oil if there is war news. The chart markup (ORBs, KPLs, bands) is taught in the strategy days. Here it is only the session.

![19:50 — GC1! five-minute, Thursday Jul 16, 2026, premarket selloff](figures/19-50.jpg)

*Figure: 19:50. `GC1!` 5-minute. The cursor sits on the push into about 8:05 a.m. ET on Thu, Jul 16, 2026, near 4,044, before the selloff that runs into 9:00 a.m.*

She describes that morning as a move from about 7:00 a.m. into 8:00 a.m., then a melt-off that lasts until about 9:00 a.m. That is the premarket gold window: you are done before the equity open.

![20:30 — GC1! five-minute, Wednesday evening Jul 15, 2026](figures/20-30.jpg)

*Figure: 20:30. The same gold contract the evening before. A vertical line sits near 7:35 p.m. ET on Wed, Jul 15, 2026. Price rejects there, then sells off through 8:00–10:00 p.m.*

She calls the early-evening reaction a rejection of the Asian opening range, with the real volume arriving around 8:00 to 9:00 p.m. ("20 to 2100" in the caption is 20:00 to 21:00). The chart shows the selloff continuing past 9:00 p.m. The rule she wants remembered is the clock, not this one gold trade: consistent Asian volume is 8:00–9:00 p.m. Eastern, not the 6:00 p.m. reopen.

</details>

<details id="prop-firm-or-self-funded">
<summary><strong>Prop firm or self-funded</strong></summary>

![21:50 — Tradeify on the prop side, NinjaTrader and Tradovate on the self-funded side](figures/21-50.jpg)

*Figure: 21:50. Two routes. Prop is Tradeify with code "Peachy". Self-funded is NinjaTrader, with an arrow to Tradovate.*

Two routes after the bootcamp:

- **Prop firm (what she recommends).** The slide names Tradeify. The captions hear it as "tradeivate". Code on the slide is `Peachy`. She says the evaluation is often 30 to 40 percent off with that code, and that a 50k account can be about $100 all-in for about $2,000 of risk. Day 9 is where she explains the rules. Treat those prices as her promo claim from this recording, and confirm them before you pay anyone.
- **Self-funded.** Two-week NinjaTrader trial, including two weeks of free data, then a cash account only if you choose it. She does not like the cash route until someone has already taken payouts from a prop account. Carrie covers the margin requirement, and the risk of posting your own capital, in the next episode.

NinjaTrader and Tradovate are the same company on this slide. She says a prop firm that only connects to Tradovate is still the same login, credentials work both ways, and the brand focus after the acquisition is NinjaTrader. Tradovate is expected to merge into it.

The order she wants:

1. Paper trade the two-week NinjaTrader trial.
2. Keep paper trading if you are not ready.
3. Then a prop evaluation.
4. A cash account only after prop payouts.

</details>

<details id="what-comes-next">
<summary><strong>What comes next</strong></summary>

Carrie follows this video. She day trades futures in the premarket and also swing trades options and stocks. Her episode goes deeper on tick value per product and on margin if you insist on the self-funded route.

</details>

## Summary

- Futures here means day trading. Swings stay in stocks and options.
- The comparison that matters: no theta, nearly 23-hour access, and leverage that is only tolerable on micros or inside a prop account with a hard loss limit.
- Chart `ES1!`, `NQ1!`, `GC1!` and put an M in front (`MES`, `MNQ`, `MGC`) until the dollar value of a tick is boring.
- ES is $12.50 per tick and $50 per point. The caption's "$1250" is the slide's $12.50.
- `ESU26` is ES, September, 2026. If you are not on the continuous symbol, trade the highest-volume month on Barchart.
- Flat before 4:45 p.m. ET. Skip 12:00–1:00 p.m. The windows she actually likes are 6:00–7:00 a.m. (done before 9:15), 10:00 a.m.–12:00 p.m., and 8:00–9:00 p.m. for Asia.
- Paper trade NinjaTrader before you pay for a prop evaluation.

## References

- [Raw transcript](../../Transcripts/transcripts-txt/01-Intro%20to%20Futures.txt)
- [Lesson video](../../Videos/1-Intro-to-Futures.mp4)
- [Peachy Investor on Whop](https://whop.com/the-peachy-investor/exp_SXclVo5OHByVJv/app/)
- [Investopedia: Futures](https://www.investopedia.com/terms/f/futures.asp)
- [Investopedia: Theta](https://www.investopedia.com/terms/t/theta.asp)
- [CME Group: Contract month codes](https://www.cmegroup.com/month-codes.html)
- [Barchart futures](https://www.barchart.com/futures)
