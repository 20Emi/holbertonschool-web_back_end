export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(Newamount) {
    this._amount = Newamount;
  }

  get currency() {
    return this._currency;
  }

  set currency(NewCurrency) {
    this._currency = NewCurrency;
  }

  displayFullPrice() {
    return `${this._amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
