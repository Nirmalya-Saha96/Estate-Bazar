const HDWalletProvider = require("@truffle/hdwallet-provider");
const Web3 = require("web3");
const compiledcreatecamp=require("./build/Factory.json");

const mnemonicPhrase = "prize verify carpet deposit game round burden cabin general boil topic world";
let provider = new HDWalletProvider(mnemonicPhrase,"https://sepolia.infura.io/v3/9b837c8368e14ac099b637e111094401");

const web3= new Web3(provider);

let address;

const deploy=async()=>{
    //get all address;
    address=await web3.eth.getAccounts();
    //instance of deployble contract;
    const campaignInstance=new web3.eth.Contract(compiledcreatecamp.abi);
    //deploy contract to rinckby net work
    const campaign=await campaignInstance.deploy({data:compiledcreatecamp.evm.bytecode.object}).send({
        from: address[0],
        gass:'1000000'
    });
    
    
    console.log(campaign.options.address)
}

deploy();