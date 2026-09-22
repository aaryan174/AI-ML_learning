let num1 = Number(prompt("enter the number"));
let num2= Number(prompt("enter the number"));
let num3= Number(prompt("enter the number"));

if(num1 > num2 && num1 > num3){
    console.log(`the number is ${num1} larger`);
}else if(num2> num1 && num2>num3){
    console.log(`the number is ${num2}is greater `);
}else if(num1 === num2 === num3){
    console.log("all are equal")
}else{
    console.log("the num3 is greater")
}

let sum1 = 0;
for(let i=1;i<=10;i++){
    console.log(sum + i);
}
let sum = 0;
for(let i=1; i<=20;i++){
    if(i%2===0){
        sum = sum +i
        console.log(sum)
    }
}