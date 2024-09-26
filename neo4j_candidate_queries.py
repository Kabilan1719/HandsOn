from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
username = "neo4j"
password = "Csk2024@"

class CandidateQueryExecutor:

    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]
executor = CandidateQueryExecutor(uri, username, password)

def get_all_candidates():
    query = """
    MATCH (c:Candidate)
    RETURN c.name AS name, c.email AS email;
    """
    return executor.execute_query(query)

def get_candidates_and_colleges():
    query = """
    MATCH (c:Candidate)-[:STUDIED_AT]->(col:College)
    RETURN c.name AS candidate_name, col.name AS college_name;
    """
    return executor.execute_query(query)

def get_candidates_by_skill(skill):
    query = """
    MATCH (c:Candidate)-[:HAS_SKILL]->(s:Skill {name: $skill})
    RETURN c.name AS candidate_name, c.email AS email;
    """
    return executor.execute_query(query, parameters={"skill": skill})

def get_candidates_by_college(college):
    query = """
    MATCH (c:Candidate)-[:STUDIED_AT]->(col:College {name: $college})
    RETURN c.name AS candidate_name, c.email AS email;
    """
    return executor.execute_query(query, parameters={"college": college})

def get_candidates_by_year(year):
    query = """
    MATCH (c:Candidate)-[:PASSED_OUT]->(y:Year_of_Passout {year: $year})
    RETURN c.name AS candidate_name, c.email AS email;
    """
    return executor.execute_query(query, parameters={"year": year})

def get_candidates_by_degree(degree):
    query = """
    MATCH (c:Candidate)-[:HAS_DEGREE]->(d:Degree {type: $degree})
    RETURN c.name AS candidate_name, c.email AS email;
    """
    return executor.execute_query(query, parameters={"degree": degree})

def get_candidate_relationships(candidate_name):
    query = """
    MATCH (c:Candidate {name: $candidate_name})-[r]->(n)
    RETURN c.name AS candidate_name, type(r) AS relationship, n;
    """
    return executor.execute_query(query, parameters={"candidate_name": candidate_name})

def get_candidates_by_multiple_skills(skill1, skill2):
    query = """
    MATCH (c:Candidate)-[:HAS_SKILL]->(s1:Skill {name: $skill1}),
          (c)-[:HAS_SKILL]->(s2:Skill {name: $skill2})
    RETURN c.name AS candidate_name, c.email AS email;
    """
    return executor.execute_query(query, parameters={"skill1": skill1, "skill2": skill2})

candidates = get_all_candidates()

candidates_with_python = get_candidates_by_skill("Python")
print("Candidates with Python:", candidates_with_python)

executor.close()
