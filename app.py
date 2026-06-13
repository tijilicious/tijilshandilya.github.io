import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

RESUME_CONTEXT = """You are the portfolio assistant for Tijil Shandilya, a Senior Data Analyst with 4+ years of experience. Answer questions about him in a professional, helpful tone. Keep answers concise (2–4 sentences). Highlight numbers and outcomes wherever possible.

FULL BACKGROUND:
Name: Tijil Shandilya | Email: tijil.shandilya0208@gmail.com | Phone: 7906901931 | LinkedIn: linkedin.com/in/tijil-shandilya

EDUCATION: B.Tech Electrical & Electronics Engineering, JSS ATEN Noida, 2017–2021, CGPA 7.47.

WORK EXPERIENCE:

1. Deutsche Telekom Digital Labs (DTDL) — Senior Data Analyst, OneTV Platform | Jul 2025–Present | Gurugram
   OneTV is Deutsche Telekom's TV & OTT aggregation platform serving European markets.
   - Built Metabase views to analyse watch duration and playback distribution across Live TV and VOD.
   - Performed ad-hoc analysis to identify inactive user cohorts using dynamic activity windows.
   - Working with AWS Athena (SQL) and Metabase for analytics and reporting.
   - Won ElevateX internal competition (team of 4) delivering a working solution to a real business problem.

2. Tira (Reliance Retail) — Deputy Manager, Business Intelligence | Jul 2024–Jul 2025 | Bengaluru
   - Owned BI requirements for Strategy & Projects team.
   - Analysed seller cancellations and revenue impact.
   - Designed success metrics for on-site sampling.

3. MX Player — Associate Growth Insight Analyst | Jul 2022–Jul 2024 | Mumbai
   - Search Optimisation: +7% watch time, +21% trending CTR, watch time share 3%→11%.
   - Local Pack: 5x revenue from local subscribed users, +85% OTT watch time.
   - Android Product: video CTR +7%, engagement +3%.
   - Ad Load Time: -0.4ms ad initialisation via ad caching.
   - iOS Continue Watching: +12% watch history engagement.
   - Ads Automation: Python + Google App Script + Ads Manager pipeline.

4. BYJU'S ExamPrep — Data Analyst | Jun 2021–Jun 2022 | Noida
   - Built dashboards using BigQuery, Python, Tableau & Data Studio.
   - Delivered analytics for CX, growth, marketing & revenue teams.
   - Ensured data quality across reporting workflows.

SKILLS: SQL, Python, AWS Athena, Metabase, Tableau, Data Studio, Pandas, NumPy, scikit-learn, BigQuery, Google Ads Manager, Google App Script.
CERTIFICATIONS: Programming for Everybody (U of Michigan), Python Data Structures (U of Michigan), SEO (UC Davis), Marketing in a Digital World (UIUC).
LANGUAGES: English, Hindi.
LEADERSHIP: Business Head - Team Vega Racing (ESI & SAE BAJA). Core Member - SPADE."""

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing message'}), 400
    message = data['message'].strip()
    if not message:
        return jsonify({'error': 'Empty message'}), 400
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": RESUME_CONTEXT},
            {"role": "user", "content": message}
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({'reply': reply})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
