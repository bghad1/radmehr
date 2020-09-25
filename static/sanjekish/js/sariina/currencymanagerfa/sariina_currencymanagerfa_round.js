//flag - we already updated Product.Config
var extendProductConfigformatPriceTrigged = false;
var sariinaCurrencyManagerFaJsConfig = sariinaCurrencyManagerFaJsConfig || {};
//calling this function will update Product.Config to our formatPrice

String.prototype.replaceArray = function(find, replace) {
  var replaceString = this;
  for (var i = 0; i < find.length; i++) {
    replaceString = replaceString.replace(new RegExp(find[i], 'g'), replace[i]);
  }
  return replaceString;
};

function replaceCharacters(value) {
    var en = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    var fa = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];

    return value.replaceArray(en, fa);
}

function extendProductConfigformatPrice() {
    if (typeof(Product) != "undefined") {
        if (!extendProductConfigformatPriceTrigged) {
            extendProductConfigformatPriceTrigged = true;

            Product.Config.prototype = Object.extend(Product.Config.prototype, {
                formatPrice:function (price, showSign) {
                    var str = '';
                    price = parseFloat(price);
                    if (showSign) {
                        if (price < 0) {
                            str += '-';
                            price = -price;
                        }
                        else {
                            str += '+';
                        }
                    }

                    var roundedPrice = (Math.round(price * 100) / 100).toString();

                    if (this.prices && this.prices[roundedPrice]) {
                        str += this.prices[roundedPrice];
                    } else {
                        precision = 2;
                        if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
                            if (typeof(sariinaCurrencyManagerFaJsConfig.precision) != "undefined") {
                                precision = sariinaCurrencyManagerFaJsConfig.precision;
                            }
                        }
                        if (typeof(optionsPrice) != "undefined") {
                            if (typeof(optionsPrice.priceFormat) != "undefined") {
                                precision = optionsPrice.priceFormat.requiredPrecision;
                            }
                        }
                        if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
                            if (typeof(sariinaCurrencyManagerFaJsConfig.cutzerodecimal) != "undefined") {
                                if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal != 0) {
                                    if (price - Math.round(price) == 0) {
                                        precision = 0;
                                    }
                                }
                            }
                        }

                        if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
                            if (typeof(sariinaCurrencyManagerFaJsConfig.min_decimal_count) != "undefined") {
                                if (sariinaCurrencyManagerFaJsConfig.min_decimal_count < precision) {
                                    for (var testPrecision = sariinaCurrencyManagerFaJsConfig.min_decimal_count;
                                         testPrecision < precision; testPrecision++) {
                                        //abs for 0.00199999999 or 1.1000000000001 fix
                                        if (Math.abs(Math.round(price * Math.pow(10, testPrecision))
                                            - price * Math.pow(10, testPrecision))<0.0000001) {
                                            precision = testPrecision;
                                            break;
                                        }
                                    }
                                }
                            }
                        }


                        if (precision > 0) {
                            str += this.priceTemplate.evaluate({price:price.toFixed(precision)});
                        }
                        else {
                            price = price.toFixed(0);
                            if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
                                if (typeof(sariinaCurrencyManagerFaJsConfig.cutzerodecimal) != "undefined") {
                                    if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal != 0) {
                                        if (typeof(sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix) != "undefined") {
                                            if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix.length > 0) {
                                                price = price + "" + sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix;
                                            }
                                        }
                                    }
                                }
                            }
                            str += this.priceTemplate.evaluate({price:price});
                        }
                    }

                    str = replaceCharacters(str);
                    return str;
                }
            });

            if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal > 0) {
                Product.OptionsPrice.prototype = Object.extend(Product.OptionsPrice.prototype, {formatPrice:function (price) {
                    var tmpPriceFormat = Object.clone(this.priceFormat);
                    if (price - parseInt(price) == 0) {
                        tmpPriceFormat.precision = 0;
                        tmpPriceFormat.requiredPrecision = 0;
                    }
                    if (tmpPriceFormat.precision < 0) {
                        tmpPriceFormat.precision = 0;
                    }
                    if (tmpPriceFormat.requiredPrecision < 0) {
                        tmpPriceFormat.requiredPrecision = 0;
                    }
                    var price2return = formatCurrency(price, tmpPriceFormat);

                    return replaceCharacters(price2return);
                }});
            }
        }
    }
}

extendProductConfigformatPrice();

try {

    originalFormatCurrency = window.formatCurrency;

    window.formatCurrency = function (price, originalFormat, showPlus) {
        var format = Object.clone(originalFormat);

        //zeroSymbol
        //JS round fix
        price = Math.round(price * Math.pow(10, format.precision)) / Math.pow(10, format.precision);
        if (price - Math.round(price) != 0) {
            if (Math.abs(price - Math.round(price)) < 0.00000001) {
                price = 0;
            }
        }
        if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
            if (price == 0) {
                if (typeof(sariinaCurrencyManagerFaJsConfig.zerotext) != "undefined") {
                    return sariinaCurrencyManagerFaJsConfig.zerotext;
                }
            }
        }
        //cut zero decimal
        if (price - Math.round(price) == 0) {
            if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
                if (typeof(sariinaCurrencyManagerFaJsConfig.cutzerodecimal) != "undefined") {
                    if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal != 0) {
                        format.precision = 0;
                        format.requiredPrecision = 0;

                        var for_replace = originalFormatCurrency(price, format, showPlus);
                        format.pattern = "%s";
                        var replaced_part = originalFormatCurrency(price, format, showPlus);
                        format.pattern = originalFormat.pattern;
                        if (typeof(sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix) != "undefined") {
                            if (sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix.length > 0) {
                                return for_replace.replace(replaced_part, replaced_part + ""
                                    + sariinaCurrencyManagerFaJsConfig.cutzerodecimal_suffix);
                            }
                        }
                    }
                }
            }
        }

        if (typeof(sariinaCurrencyManagerFaJsConfig) != "undefined") {
            if (typeof(sariinaCurrencyManagerFaJsConfig.min_decimal_count) != "undefined") {
                if (sariinaCurrencyManagerFaJsConfig.min_decimal_count < format.precision) {
                    for (var testPrecision = sariinaCurrencyManagerFaJsConfig.min_decimal_count;
                         testPrecision < format.precision; testPrecision++) {
                        //abs for 0.00199999999 or 1.1000000000001 fix
                        if (Math.abs(Math.round(price * Math.pow(10, testPrecision))
                            - price * Math.pow(10, testPrecision))<0.0000001) {
                            format.precision = testPrecision;
                            format.requiredPrecision = testPrecision;
                            break;
                        }
                    }
                }
            }
        }


        return formatCurrencyET(price, format, showPlus);
        //if(format.precision<0)format.precision=0;
        //if(format.requiredPrecision<0)format.requiredPrecision=0;
        /*return originalFormatCurrency(price, format, showPlus);*/


    };


    function formatCurrencyET(price, format, showPlus) {
        var precision = isNaN(format.precision = (format.precision)) ? 2 : format.precision;
        var requiredPrecision = isNaN(format.requiredPrecision = (format.requiredPrecision)) ? 2 : format.requiredPrecision;

        //precision = (precision > requiredPrecision) ? precision : requiredPrecision;
        //for now we don't need this difference so precision is requiredPrecision
        precision = requiredPrecision;

        var integerRequired = isNaN(format.integerRequired = Math.abs(format.integerRequired)) ? 1 : format.integerRequired;

        var decimalSymbol = format.decimalSymbol == undefined ? "," : format.decimalSymbol;
        var groupSymbol = format.groupSymbol == undefined ? "." : format.groupSymbol;
        var groupLength = format.groupLength == undefined ? 3 : format.groupLength;

        var s = '';

        if (showPlus == undefined || showPlus == true) {
            s = price < 0 ? "-" : ( showPlus ? "+" : "");
        } else if (showPlus == false) {
            s = '';
        }

        var i = parseInt(price = Math.abs(+price || 0).toFixed(precision)) + "";
        var pad = (i.length < integerRequired) ? (integerRequired - i.length) : 0;
        while (pad) {
            i = '0' + i;
            pad--;
        }
        j = (j = i.length) > groupLength ? j % groupLength : 0;
        re = new RegExp("(\\d{" + groupLength + "})(?=\\d)", "g");

        /**
         * replace(/-/, 0) is only for fixing Safari bug which appears
         * when Math.abs(0).toFixed() executed on "0" number.
         * Result is "0.-0" :(
         */
        if (precision < 0) {
            precision = 0;
        }
        var r = (j ? i.substr(0, j) + groupSymbol : "") + i.substr(j).replace(re, "$1" + groupSymbol) + (precision ? decimalSymbol + Math.abs(price - i).toFixed(precision).replace(/-/, 0).slice(2) : "")
        var pattern = '';
        if (format.pattern.indexOf('{sign}') == -1) {
            pattern = s + format.pattern;
        } else {
            pattern = format.pattern.replace('{sign}', s);
        }

        result = pattern.replace('%s', r).replace(/^\s\s*/, '').replace(/\s\s*$/, '');
        return replaceCharacters(result);
    }




}
catch (e) {
    //do nothing
}


