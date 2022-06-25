
class Validator {
    static checkName(name) {
        return name !== "";
    }

    static checkPhone(phone) {
        return phone.replace(/\D/g, "").length === 11;
    }

    static checkEmail(email) {
        const hasCyrillic = /[\u0400-\u04FF]+/.test(email);
        const isEmail = /\S+@\S+\.\S+/.test(email);

        return !hasCyrillic && isEmail;
    }

    static checkInn(inn) {
        return inn.length === 10;
    }

    static checkPassword(password) {
        const min6 = password.length >= 6;
        const hasCyrillic = /[\u0400-\u04FF]+/.test(password);

        return min6 && !hasCyrillic;
    }
}


export default Validator;
