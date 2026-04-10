---
name: daily-report
description: "generate daily todo tasks"
---

# Daily Report Skill

## Trigger
When user says `daily report` or `daily report → send to slack`

## Format
Report — {date}
- {task description} `Done`
- {task description} `Done`

## Rules
- Plain list, no sections, no headers
- Each line ends with `Done` in backticks
- Date format: April 9, 2026
- No emojis, no bold, no categories
- Short one-line descriptions per task

## Slack Flow
1. Send draft to C070CSSUUNL (my-reports) first
2. Wait for user confirmation ("ок", "ok", "отправь", "all good", etc.)
3. On confirmation — send to C04R64SB2RL (general channel)

## Example
Report — April 9, 2026
- Reduced CodeBuild time from ~25 min to ~2.5 min by implementing S3-based gem cache system `Done`
- Cache works by hashing Gemfile.lock — on HIT skips bundle install entirely `Done`
- Investigated beta deploy crash caused by devise gem not loading for AdminUser `Done`
