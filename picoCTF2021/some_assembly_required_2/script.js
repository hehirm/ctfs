const _0x6d8f = ['copy_char', 'value', '207aLjBod', '1301420SaUSqf', '233ZRpipt', '2224QffgXU', 'check_flag', '408533hsoVYx', 'instance', '278338GVFUrH', 'Correct!', '549933ZVjkwI', 'innerHTML', 'charCodeAt', './aD8SvhyVkb', 'result', '977AzKzwq', 'Incorrect!', 'exports', 'length', 'getElementById', '1jIrMBu', 'input', '615361geljRK'];
const _0x5c00 = function (_0x58505a, _0x4d6e6c) {
  _0x58505a = _0x58505a - 0xc3;
  let _0x6d8fc4 = _0x6d8f[_0x58505a];
  return _0x6d8fc4;
};
(function (_0x12fd07, _0x4e9d05) {
  while (true) {
    try {
      const _0x1bb902 = -parseInt(_0x5c00(0xc8)) * -parseInt(_0x5c00(0xc9)) + -parseInt(_0x5c00(0xcd)) + parseInt(_0x5c00(0xcf)) + parseInt(_0x5c00(0xc3)) + -parseInt(_0x5c00(0xc6)) * parseInt(_0x5c00(0xd4)) + parseInt(_0x5c00(0xcb)) + -parseInt(_0x5c00(0xd9)) * parseInt(_0x5c00(0xc7));
      if (_0x1bb902 === _0x4e9d05) {
        break;
      } else {
        _0x12fd07.push(_0x12fd07.shift());
      }
    } catch (_0x4f8a) {
      _0x12fd07.push(_0x12fd07.shift());
    }
  }
})(_0x6d8f, 0x4bb06);
let exports;
(async () => {
  let _0x1adb5f = await fetch("./aD8SvhyVkb");
  let _0x355961 = await WebAssembly.instantiate(await _0x1adb5f.arrayBuffer());
  let _0x5c0ffa = _0x355961["instance"];
  exports = _0x5c0ffa["exports"];
})();
function onButtonPress() {
  // let _0x5f4170 = document["getElementById"]("input")["value"];
  let input_value = document.getElementById("input").value;
  _0x19d3ca = i
  _0x5f4170 = input_value
  for (let i = 0; i < input_value.length; i++) {
    //exports[_0x5c00(0xc4)](input_value[_0x5c00(0xd1)](i), i);
    //exports["copy_char"](input_value["charCodeAt"](i), i)
    exports.copy_char(input_value.charCodeAt(i), i);
  }
  exports.copy_char(0, input_value.length);
  if (exports.check_flag() == 1) {
    document.getElementById("result").innerHTML = "Correct!";
  } else {
    document.getElementById("result").innerHTML = "Incorrect!";
  }
}
