from flask import Flask, request, jsonify, render_template
import pandas as pd
from neo4j import GraphDatabase

app = Flask(__name__)

dataset_path = 'sample_candidates_data.csv'
df = pd.read_csv(dataset_path)

neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_password = "Csk2024@"
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_candidates():
    query = request.args.get('query')
    filtered_data = df[df['Skills'].str.contains(query, case=False, na=False)]
    
    # Example: Add candidates to Neo4j database
    with driver.session() as session:
        for _, row in filtered_data.iterrows():
            session.run(
                "CREATE (c:Candidate {name: $name, email: $email, college: $college, year: $year, degree: $degree, skills: $skills})",
                name=row['Name'], email=row['Email'], college=row['College'], 
                year=row['Year of Passout'], degree=row['Degree'], skills=row['Skills']
            )

    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
