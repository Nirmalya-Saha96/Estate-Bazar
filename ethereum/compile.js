const fs=require("fs-extra");
const path=require("path");
const solc=require("solc");

const buildPath=path.resolve(__dirname,"build");
fs.removeSync(buildPath);
const contractPath=path.resolve(__dirname,"contract","Auctioninfo.sol");
const source=fs.readFileSync(contractPath,"utf-8");

var input = {
  language: 'Solidity',
  sources: {
    'Auctioninfo.sol': {
      content: source
    }
  },
  settings: {
    outputSelection: {
      '*': {
        '*': ['*']
      }
    }
  }
};

var output = JSON.parse(solc.compile(JSON.stringify(input)));
output=(output.contracts["Auctioninfo.sol"]);

fs.ensureDirSync(buildPath);

for(let contract in output){
  fs.outputJsonSync(
    path.resolve(buildPath,contract+'.json'),
    output[contract]
  )
}