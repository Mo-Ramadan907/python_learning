// console.log("hello world");
// const m = "61fdb4d9f1e946d8aa7143657252506";
// const city = 'london';
// const d = 3;
let d = null;
async function getWeather(city) {
    const apiKey = '61fdb4d9f1e946d8aa7143657252506';
    const l = city;
    const days = 3;
    const url = `https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=${l}&days=${days}`;

    const res = await fetch(url);
    const data = await res.json();
    d = data.forecast;
}
async function getCityAndCountry(){
   const res =await fetch('https://ipapi.co/json/')
    const data = await res.json();
    const city = data.city;
    const country = data.country;
    d = city
    return [city,country]
}
function buildDiv(data){
    let div = document.createElement('div');
    div.classList.add('ele');
    
}
async  function main(){

    await getWeather();
    console.log(d);
}

main()
