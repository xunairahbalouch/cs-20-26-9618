const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 8080;

// MCP config
const MCP_TOOLS = [
    {
        name: "get_farm_history",
        description: "Retrieve previous crop diagnoses and farm records",
        inputSchema: { type: "object", properties: {} }
    },
    {
        name: "diagnose_crop",
        description: "Analyze crop health and provide recommendations",
        inputSchema: {
            type: "object",
            properties: {
                cropType: { type: "string" },
                symptoms: { type: "string" }
            },
            required: ["cropType", "symptoms"]
        }
    }
];

//MCP endpoint
app.post('/mcp', async (req, res) => {
    const { method, params, id } = req.body;

    // 1. Tool Discovery
    if (method === "tools/list") {
        return res.json({
            jsonrpc: "2.0",
            id,
            result: { tools: MCP_TOOLS }
        });
    }

    //  Tool Execution
    if (method === "tools/call") {
        const { name, arguments: args } = params;

        try {
            if (name === "get_farm_history") {
                const history = await mongoose.connection.db.collection('diagnoses').find().limit(5).toArray();
                return res.json({
                    jsonrpc: "2.0",
                    id,
                    result: { content: [{ type: "text", text: JSON.stringify(history) }] }
                });
            }

            if (name === "diagnose_crop") {
                return res.json({
                    jsonrpc: "2.0",
                    id,
                    result: { content: [{ type: "text", text: `Diagnosis for ${args.cropType}: Possible blight. Recommendation: Apply fungicide.` }] }
                });
            }
        } catch (error) {
            return res.status(500).json({ jsonrpc: "2.0", id, error: { message: error.message } });
        }
    }

    res.status(404).json({ jsonrpc: "2.0", id, error: { message: "Method not found" } });
});

// existing endpoints
app.get('/', (req, res) => res.status(200).send('Wheatee MCP Server Active'));
app.get('/history', async (req, res) => {
    try {
        const history = await mongoose.connection.db.collection('diagnoses').find().toArray();
        res.status(200).json({ success: true, data: history });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Start Server
app.listen(PORT, '0.0.0.0', () => {
    console.log(`MCP Server listening on port ${PORT}`);
});

// Background DB Connection
const MONGO_URI = "mongodb+srv://younassadat05_db_user:GQDR8nnBs2NPK3EL@wheatee-cluster.ayneck3.mongodb.net/wheatee_db?appName=wheatee-cluster";
mongoose.connect(MONGO_URI).catch(err => console.error("DB connection error:", err));
