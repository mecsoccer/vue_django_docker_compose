const arr = new Array(10).fill(1)
const user = 3

const newArr = arr.map((el, idx) => {
    const x = (idx + 1)%3 === 0 ? "A" : (idx + 1)%2 === 0 ? "B" : "C"
    const y = (idx + 1)%3 === 0 ? 2.56 : (idx + 1)%2 === 0 ? 3.56 : 1.56
    const z = (idx + 1)%3 === 0 ? 1.25 : (idx + 1)%2 === 0 ? 1.05 : 1.35
    return {
        "model": "ChargeSessionCost.ChargeSessionCost",
        "pk": idx + 111,
        "fields": {
            "user_info": user,
            "location": "Station " + x,
            "energy_kWh": y,
            "cost": z,
            "charge_datetime": "2023-02-10 15:51:27.993955+00"
        }
    }
})

console.log(JSON.stringify(newArr))
