CREATE TABLE IF NOT EXISTS predictions_log (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    prediction VARCHAR(50) NOT NULL,
    confidence FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
