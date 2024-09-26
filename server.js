const express = require('express');
const neo4j = require('neo4j-driver');
const cors = require('cors');

const app = express();
app.use(cors());  // To allow cross-origin requests

const driver = neo4j.driver(
  'bolt://localhost:7687', // Ensure this is correct
  neo4j.auth.basic('neo4j', 'Csk2024@') // Replace with your credentials
);

const session = driver.session();

// Route to fetch data from Neo4j
app.get('/getNetworkData', async (req, res) => {
  try {
    const result = await session.run(`
      MATCH (n)-[r]->(m) 
      RETURN n.name as from, m.name as to, n.skills as fromSkills, m.skills as toSkills
    `);

    const networkData = result.records.map(record => ({
      from: record.get('from'),
      to: record.get('to'),
      fromSkills: record.get('fromSkills'),
      toSkills: record.get('toSkills'),
    }));

    res.json(networkData);
  } catch (error) {
    console.error('Error fetching data from Neo4j:', error);
    res.status(500).json({ error: 'Failed to fetch data' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});