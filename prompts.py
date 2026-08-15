SUMMARY_PROMPT_V1 = """
Summarize this loan application.
{letter_text}
"""


SUMMARY_PROMPT = """
You are an assistant to a microfinance loan officer.

Summarize the following loan application in 3-4 sentences.

Requirements:
- Be factual and neutral.
- Use only information explicitly stated in the application.
- Do not invent, assume, or infer details.
- Include the applicant's name, requested loan amount, purpose of the loan,
  relevant financial information, collateral or guarantor information,
  and repayment information when provided.
- If important information is missing, do not guess it.
- Keep the summary concise and suitable for a busy loan officer.

Loan application:

{letter_text}
"""


EXTRACT_PROMPT = """
You are extracting structured information from a loan application letter.

Return ONLY a valid JSON object with EXACTLY these six keys:

{{
  "applicant_name": "string",
  "amount_ghs": "number",
  "purpose": "string",
  "monthly_profit_ghs": "number or null",
  "has_collateral_or_guarantor": "boolean",
  "repayment_months": "number or null"
}}

Rules:
1. Use only information explicitly stated in the letter.
2. Do not guess, infer, or invent information.
3. If a field is not stated in the letter, use null.
4. amount_ghs, monthly_profit_ghs, and repayment_months must be numbers,
   not strings.
5. Convert repayment periods stated in years into months. For example,
   "one year" means 12 months and "two years" means 24 months.
6. has_collateral_or_guarantor must be true if the letter explicitly
   mentions collateral or a guarantor, and false if the letter explicitly
   says there is none.
7. Return ONLY the JSON object. Do not include explanations, markdown,
   or ```json fences.

Here is one example:

LETTER:
Dear Loan Officer,

My name is Abena Owusu and I run Sweet Crumbs Bakery in Accra.
I am requesting GHS 10,000 to purchase a commercial oven and additional
baking supplies.
The bakery makes approximately GHS 1,500 profit each month.
I can repay GHS 700 per month for 15 months.
My mother will act as my guarantor.

Thank you.

JSON:
{{
  "applicant_name": "Abena Owusu",
  "amount_ghs": 10000,
  "purpose": "purchase a commercial oven and additional baking supplies",
  "monthly_profit_ghs": 1500,
  "has_collateral_or_guarantor": true,
  "repayment_months": 15
}}

Now extract the information from this loan application:

{letter_text}
"""


BRIEF_PROMPT = """
You are an assistant supporting a microfinance loan officer.

Prepare a concise, neutral decision-support brief using ONLY information
explicitly stated in the original loan application and the extracted JSON.

IMPORTANT:
- Do not invent, assume, speculate, or infer facts.
- Do not make judgments based on age, gender, location, writing style,
  or other personal characteristics.
- Do not treat an applicant's claims as verified facts. Clearly identify
  them as claims when relevant.
- Do not describe something as "stable", "significant", "high risk",
  "unrealistic", or similar unless the letter itself provides evidence
  supporting that characterization.
- If information is not provided, classify it as MISSING INFORMATION,
  not as a risk.
- Do not introduce generic business risks that are not directly supported
  by the application.
- Do not repeat the same point in multiple sections.
- Do not show your reasoning process or intermediate steps.

Your output MUST contain exactly these four headings and no additional
headings:

## Strengths
- List positive factors explicitly supported by the application.
- Clearly distinguish verified information from claims made by the applicant.

## Risks / Red Flags
- List concerns directly supported by information in the application,
  such as existing business difficulties, lack of collateral, or an
  unclear repayment proposal.
- Do not turn missing information into a risk.

## Missing Information
- List important information that is not provided but would help the loan
  officer assess the application.
- Do not list information that is already stated in the letter.

## Suggested Next Step
- Recommend practical actions such as requesting documents, verifying
  financial information, inviting the applicant for an interview,
  requesting a business plan, or flagging the application for senior review.
- Do NOT recommend "approve" or "reject".
- The final lending decision must always be made by a human loan officer.

Keep the entire brief concise and factual.

Original loan application:
{letter_text}

Extracted information:
{extracted_json}
"""
