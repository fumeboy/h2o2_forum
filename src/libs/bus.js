const methods = {};
// 用法
// BUS.register('method_1', this.method_1); 注册方法
// BUS.invoke('method_1', params, param_2); 使用方法
module.exports = {
    register: function(name, func) {
        methods[name] = func;
    },
    invoke: function(name, ...args) {
        let method = methods[name];
        if (!method) return;
        method.apply(null, args);
    }
};
