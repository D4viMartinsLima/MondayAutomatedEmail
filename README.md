# 💌 Monday Motivation Email Bot

> A simple **Python automation app** that sends a random motivational quote via email every Monday morning.  
> Built using **smtplib** for email delivery and **datetime** to schedule weekly execution.

## 🧩 Technologies and Tools Used

- **Python 3.10+**
- **smtplib** — for sending emails through Gmail’s SMTP server
- **datetime** — to check the current weekday
- **random** — to select a random quote from the list
- **text files** — to store motivational quotes (`quotes.txt`)

## ⚙️ Main Features

- Automatically checks the current weekday using the `datetime` module.  
- Sends an inspirational quote only when it’s Monday (or any desired weekday).  
- Selects a random quote from the `quotes.txt` file to keep messages unique.  
- Uses Gmail’s SMTP server with TLS encryption for secure email delivery.  
- Fully automated — can be scheduled to run weekly using a task scheduler or cron job.

## 🖥️ Demonstration

```bash
📁 Monday Motivation/
├── main.py
└── quotes.txt

💬 Example email sent:
Subject: Monday Motivation  
Believe you can and you're halfway there.

