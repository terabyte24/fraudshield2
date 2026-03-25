const fs = require("fs");
const path = require("path");

async function main() {
  const FraudLedger = await ethers.getContractFactory("FraudLedger");
  const fraudLedger = await FraudLedger.deploy();

  await fraudLedger.waitForDeployment();
  const address = await fraudLedger.getAddress();
  
  console.log(`FraudLedger deployed to: ${address}`);

  const abiPath = path.join(__dirname, "../artifacts/contracts/FraudLedger.sol/FraudLedger.json");
  const abiJson = JSON.parse(fs.readFileSync(abiPath, "utf8"));

  const contractInfo = {
    address: address,
    abi: abiJson.abi
  };

  const outDir = path.join(__dirname, "../../Money-Muling/detection");
  if (!fs.existsSync(outDir)) {
      fs.mkdirSync(outDir, { recursive: true });
  }

  const outPath = path.join(outDir, "contract_info.json");
  fs.writeFileSync(outPath, JSON.stringify(contractInfo, null, 2));
  
  console.log("contract_info.json written for Python.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
