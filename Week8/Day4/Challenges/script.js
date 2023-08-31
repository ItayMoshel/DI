const apiKey = '3bcae8a0243fe4bfccfb91d6';
const supportedCurrenciesEndpoint = 'https://api.apilayer.com/exchangerates_data/latest';

const fromCurrencySelect = document.getElementById('fromCurrency');
const toCurrencySelect = document.getElementById('toCurrency');
const amountInput = document.getElementById('amount');
const convertBtn = document.getElementById('convertBtn');
const switchBtn = document.getElementById('switchBtn');
const resultParagraph = document.getElementById('result');

async function fetchCurrencies() {
    try {
        const response = await fetch(`${supportedCurrenciesEndpoint}?apikey=${apiKey}`);
        const data = await response.json();

        const currencies = Object.keys(data.rates);
        populateCurrencySelects(currencies);
    } catch (error) {
        console.error('Error fetching currencies:', error);
    }
}

function populateCurrencySelects(currencies) {
    currencies.forEach(currency => {
        const fromOption = document.createElement('option');
        fromOption.value = currency;
        fromOption.textContent = currency;
        fromCurrencySelect.appendChild(fromOption);

        const toOption = document.createElement('option');
        toOption.value = currency;
        toOption.textContent = currency;
        toCurrencySelect.appendChild(toOption);
    });
}

async function convertCurrency() {
    const fromCurrency = fromCurrencySelect.value;
    const toCurrency = toCurrencySelect.value;
    const amount = parseFloat(amountInput.value);

    if (isNaN(amount)) {
        resultParagraph.textContent = 'Please enter a valid amount.';
        return;
    }

    try {
        const response = await fetch(`https://api.apilayer.com/exchangerates_data/${fromCurrency}_${toCurrency}?apikey=${apiKey}`);
        const data = await response.json();
        const exchangeRate = data.rate;

        const convertedAmount = (amount * exchangeRate).toFixed(2);
        resultParagraph.textContent = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
    } catch (error) {
        console.error('Error converting currency:', error);
    }
}

function switchCurrencies() {
    const fromCurrencyValue = fromCurrencySelect.value;
    const toCurrencyValue = toCurrencySelect.value;

    fromCurrencySelect.value = toCurrencyValue;
    toCurrencySelect.value = fromCurrencyValue;

    convertCurrency();
}

fetchCurrencies();

convertBtn.addEventListener('click', convertCurrency);
switchBtn.addEventListener('click', switchCurrencies);
