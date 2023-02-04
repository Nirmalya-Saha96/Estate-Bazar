import web3 from "./web3";
import createCamp from "./build/Factory.json"

const address='0xBC82eC51886c9E7Bfc9c47a113932Ce4CaBD588F'
const abi=createCamp.abi;

export default new web3.eth.Contract(abi,address)