from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

job_templates = [
    "We are hiring for a remote data entry position. No experience required.",
    "Congratulations! You've been selected for a customer support role.",
    "Dear Applicant, we would like to offer you a position at our company."
]

def compute_similarity(text):
    # Embed input text
    text_emb = model.encode(text, convert_to_tensor=True)
    # Embed templates
    template_embs = model.encode(job_templates, convert_to_tensor=True)
    # Compute cosine similarities
    similarities = util.pytorch_cos_sim(text_emb, template_embs)[0].cpu().numpy()

    avg_score = float(similarities.mean()) * 100
    best_score = float(similarities.max()) * 100

    # Find the template(s) with the highest similarity
    max_sim = similarities.max()
    matched_roles = [template for template, sim in zip(job_templates, similarities) if sim == max_sim]

    # Always return avg_score and a list
    return round(avg_score, 2), matched_roles
