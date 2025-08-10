---
description: Free German-language API that predicts Queue and Priority for support tickets. Easy integration for OTOBO, Znuny, Zammad, and custom helpdesks. No auth required.
---

# 🇩🇪 German Ticket Classification API (Free)

Predict **Queue** and **Priority** for **German-language** support tickets with a single HTTP call.
This API is **free** to use and ideal for integrations with **OTOBO**, **Znuny**, **Zammad**, or custom helpdesks.

> **Language Support:** Optimized for **German** texts (subject + body).
English Model is in development, will be realeased soon.
---

## Try it out!
<OTAIPredictionDemo/>

## 📍 Endpoint

**Method:** `POST`
**URL:** `https://open-ticket-ai.com/api/german_prediction/v1/classify`
**Headers:** `Content-Type: application/json`

### Request body
```json
{
  "subject": "VPN Verbindungsproblem",
  "body": "Kann nach dem Update keine Verbindung zum Unternehmens-VPN herstellen. Vor dem letzten Update funktionierte es einwandfrei."
}
````

### Example response

```json
{
  "queue": "IT & Technology/Network Infrastructure",
  "queue_conf": 0.94,
  "priority": "high",
  "priority_conf": 0.88
}
```

> `queue_conf` and `priority_conf` are confidence scores (`0.0–1.0`).

---

## 🚀 Quick Start

### cURL

```bash
curl -X POST "https://open-ticket-ai.com/api/german_prediction/v1/classify" \
  -H "Content-Type: application/json" \
  -d '{
        "subject": "VPN Verbindungsproblem",
        "body": "Kann nach dem Update keine Verbindung zum Unternehmens-VPN herstellen. Vor dem letzten Update funktionierte es einwandfrei."
      }'
```

### JavaScript (Node.js / Browser)

```js
const res = await fetch("https://open-ticket-ai.com/api/german_prediction/v1/classify", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    subject: "VPN Verbindungsproblem",
    body: "Kann nach dem Update keine Verbindung zum Unternehmens-VPN herstellen. Vor dem letzten Update funktionierte es einwandfrei."
  })
});
const data = await res.json();
console.log(data);
```

### Python

```python
import requests

payload = {
    "subject": "VPN Verbindungsproblem",
    "body": "Kann nach dem Update keine Verbindung zum Unternehmens-VPN herstellen. Vor dem letzten Update funktionierte es einwandfrei."
}

r = requests.post(
    "https://open-ticket-ai.com/api/german_prediction/v1/classify",
    json=payload,
    timeout=30
)

print(r.json())
```

---

## 🎯 Queues

The API may return any of the following **queue labels**:

* Pets & Animals/Pet Services
* News
* IT & Technology/Security Operations
* Autos & Vehicles/Sales
* Health/Medical Services
* Home & Garden/Home Improvement
* Pets & Animals/Veterinary Care
* Health/Mental Health
* Business & Industrial/Manufacturing
* Online Communities/Forums
* Shopping/E-commerce
* Food & Drink/Groceries
* Travel & Transportation/Land Travel
* Jobs & Education/Online Courses
* Finance/Investments
* Law & Government/Government Services
* Hobbies & Leisure/Collectibles
* Online Communities/Social Networks
* Books & Literature/Non-Fiction
* Science/Environmental Science
* Hobbies & Leisure/Crafts
* Finance/Personal Finance
* Science/Research
* IT & Technology/Network Infrastructure
* Games
* Travel & Transportation/Air Travel
* Beauty & Fitness/Cosmetics
* Arts & Entertainment/Music
* Food & Drink/Restaurants
* Law & Government/Legal Advice
* Autos & Vehicles/Maintenance
* IT & Technology/Hardware Support
* Jobs & Education/Recruitment
* Books & Literature/Fiction
* Beauty & Fitness/Fitness Training
* Shopping/Retail Stores
* People & Society/Culture & Society
* Arts & Entertainment/Movies
* IT & Technology/Software Development
* Home & Garden/Landscaping
* Sports
* Real Estate

---

## ⚡ Priorities

The API predicts one of the following **priority levels**:

| Priority  | Numeric |
| --------- | ------- |
| very\_low | 0       |
| low       | 1       |
| medium    | 2       |
| high      | 3       |
| critical  | 4       |

---

## 🔌 Integration Ideas

* **OTOBO / Znuny**: Call the API on ticket creation to pre-fill Queue + Priority.
* **Custom Helpdesk**: Run it in your intake pipeline before routing/SLAs.
* **Automation**: Auto-escalate `critical` tickets or route security incidents.
* **Analytics**: Track queue distribution & priority trends over time.

---

## ✅ Best Practices

* Provide **concise, clear subjects** and **descriptive bodies** in **German**.
* Avoid very long inputs; keep under \~5,000 characters combined.
* Log and monitor results to fine-tune downstream rules.

---

## ❓ Troubleshooting

* **400 Bad Request**: `subject` or `body` missing.
* **5xx errors**: Upstream model temporarily unavailable — retry with backoff.
* Predictions look off? Ensure the text is **German** and contains enough context.

---

## 📄 Terms

* **Free** to use; please be mindful of request volume.
* We may introduce fair-use limits to keep the service healthy for everyone.
* No authentication required.

---
