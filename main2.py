import requests

TOXICITY_THRESHOLD = 0.5
while True:
    KEY = ''
    comment = raw_input('Enter a text to analyse whether it is mean or not: ')
    request = {
            "comment": {"text": comment},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY":{}
            }
        }
    resp = requests.post('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=' + KEY,
            json=request);

    response = resp.json()
    scores = response['attributeScores']
    toxicityAttrib = scores['TOXICITY']
    toxicitySummary = toxicityAttrib['summaryScore']
    toxicityProbability = float(toxicitySummary['value'])
    if toxicityProbability > TOXICITY_THRESHOLD:
        print("That is mean!")
    else:
        print("That is not mean, excellent!")
