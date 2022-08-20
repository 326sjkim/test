// 1. 인라인 함수
// 2. 지역 변수(play)제거 - 임시 변수를 질의 함수로 바꾸기 playFor
// 3. 변수 인라인 하기 VolumeCreditFor
// 4. for 문 내용을 함수로 빼내기
// 5. format 변수 제거하기 format -> 적당한 이름으로 바꾸기
// 6. 문장 슬라이드 하기
// 7. for 문 쪼개기

//import { invoice } from './data.js'
//import { plays } from './data.js'

console.log("Statement02") ; 

main();


function main() {
    let invoice = require('./invoice.json');
    let plays = require('./plays.json')

    // console.log(invoice);
    // console.log(plays);

    var result = statement(invoice, plays);
    //console.log(result);
}


function statement(invoice, plays) {
    const statementData={};
    statementData.customer = invoice[0].customer ;
    statementData.performances = (invoice[0].performances).map(enrichPerformance) ;

    //console.log("statementData : ",statementData) ;
    return renderPlainText(statementData, plays);

    function enrichPerformance(aPerformance){
        const result = Object.assign({}, aPerformance) ; //얕은 복사 수행!
        result.play = playFor(result) ;            
        return result ;
    }

    function playFor(aPerformance) {
        return plays[aPerformance.playID]
    }
}

function renderPlainText(data, plays){

    console.log("data :", data) ;
    //console.log("data.performances : ", data.performances) ;

    let result = `청구내역(고객명:${data.customer})\n`;

    //let volumeCredits = 0;
    //let totalAmount = 0; 
    for (let perf of data.performances) {
        //const play = plays[perf.playID];
        //volumeCredits = volumeCreditFor(perf)
        result += `${playFor(perf).name} : ${usd(amountFor(perf) / 100)} (${perf.audience}석) \n`;
        //totalAmount += amountFor(perf);
    }

    //let volumeCredits = totalVolumeCredits();    
    //let totalAmount = returntotalAmount(); 

    result += `총액: ${usd(returntotalAmount() / 100)}\n`
    result += `적립 포인트: ${totalVolumeCredits()}점\n`

    return result;

    
    function playFor(aPerformance) {
        //console.log(aPerformance.playID) ;
        return plays[aPerformance.playID]
    }

    function amountFor(aPerformance) {
        let thisAmount = 0;
        switch (playFor(aPerformance).type) {
            case "tragedy":
                thisAmount = 40000;
                if (aPerformance.audience > 30) {
                    thisAmount += 1000 * (aPerformance.audience - 30);
                }
                break;
            case "comedy":
                thisAmount = 30000;
                if (aPerformance.audience > 20) {
                    thisAmount += 500 * (aPerformance.audience - 20);
                }
                break;
            default:
                throw new Error(`알 수 없는 장르 : ${play.type}`);
        }

        return thisAmount; 
    }

    

    function usd(aNumber) {
        return new Intl.NumberFormat("en-US", {
            style: "currency", currency: "USD",
            minimumFractionDigits: 2
        }).format(aNumber);
    }

    function volumeCreditFor(perf) {
        let volumeCredits = 0;
        volumeCredits += Math.max(perf.audience - 30, 0);
        if ("comedy" === playFor(perf).type)
            volumeCredits += Math.floor(perf.audience / 5);
        return volumeCredits;
    }

    function totalVolumeCredits() {
        let volumeCredits = 0;
        for (let perf of data.performances)
            volumeCredits += volumeCreditFor(perf);
        return volumeCredits;
    }

    function returntotalAmount() {
        let totalAmount = 0;
        for (let perf of data.performances)
            totalAmount += amountFor(perf);
        return totalAmount;
    }

}








