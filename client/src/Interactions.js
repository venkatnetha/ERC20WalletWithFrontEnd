import {React, useState} from 'react'
import styles from './Wallet.module.css';

const Interactions = (props) => {

	const [transferHash, setTransferHash] = useState();
    const [TotoalTokensMintedForthePrice, setTotalTokensForPrice] = useState();

    async function getYelowTokensForPrice(param) {

        const url = `http://127.0.0.1:5000/`;
        console.log("inside the function");
        let response = await fetch(`${url}/compute/?tokens=${param}`,{ mode: 'cors' },
        {
          headers : { 
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Headers': 'Content-Type',
          'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE,PUT',
          'Authorization': 'Bearer key',       
          "Access-Control-Allow-Credentials" : true 
           }
    
        })
       

        //console.log(await response.json());
       // let hi = response.TokensForPrice;
       
        const fetchedLaunches = await response.json();
        console.log(fetchedLaunches);
        console.log(fetchedLaunches.TokensForPrice)
        return fetchedLaunches.TokensForPrice
    }

	const transferHandler = async (e) => {
		e.preventDefault();

        let numberOfTokensToMint = await getYelowTokensForPrice(e.target.sendAmount.value);
        console.log(numberOfTokensToMint);
        console.log("hiiiihi");
        console.log(numberOfTokensToMint.TokensForPrice);
		//let transferAmount = e.target.sendAmount.value;
		let recieverAddress = e.target.recieverAddress.value;

		let txt = await props.contract.mintYelowTokens(recieverAddress, numberOfTokensToMint);
		console.log(txt);
		setTransferHash("Transfer confirmation hash: " + txt.hash);
        setTotalTokensForPrice("The Amount of Tokens Minted for Your Price: " + numberOfTokensToMint);
	}

	return (
			<div className={styles.interactionsCard}>
				<form onSubmit={transferHandler}>
					<h3> Transfer Yelow Tokens </h3>
						<p> Reciever Address </p>
						<input type='text' id='recieverAddress' className={styles.addressInput}/>

						<p> Send Amount </p>
						<input type='number' id='sendAmount' min='0' step='1'/>

                        
						<button type='submit' className={styles.button6}>Send</button>
						<div>
							<h4>{transferHash}</h4>
						</div>
                        <div>
                            <h3>{TotoalTokensMintedForthePrice}</h3>
                        </div>
			</form>
			</div>
		)
	
}

export default Interactions;