const express = require('express');
const app = express();
app.use();

app.listen(5000, () => {
    console.log("listining on 5000");
});

app.get('/price', (req, res) => {
    const pricedata = res.json().data;
    return pricedata;
})


app.post('/pay', (req, res) => {
    const paymentdetails = req.args.payment;
    paymentdetails.json.send()
})