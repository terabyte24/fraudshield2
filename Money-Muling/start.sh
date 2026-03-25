#!/bin/bash
echo "Starting Hardhat node..."
cd ../blockchain && npx hardhat node &
HARDHAT_PID=$!
sleep 3
echo "Deploying contract..."
npx hardhat run scripts/deploy.js --network localhost
echo "Starting Flask..."
cd ../Money-Muling && python app.py
trap "kill $HARDHAT_PID" EXIT
