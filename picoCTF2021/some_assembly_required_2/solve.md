# picoCTF2021 Some Assembly Required 2 Write Up

## Description

> [http://mercury.picoctf.net:7319/index.html](http://mercury.picoctf.net:7319/index.html)

This challenge is a continuation of Some Assembly Required 1.
## Solution

**Notes**:
- I did not solve this challenge independently. In particular the write up by [Dvd848](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Some_Assembly_Required_2.md) was extremely helpful in making my own (there are many similarities).
- I still do not fully understand why the web assembly decompilation produces the function `copy` as opposed to `copy_char` which is what is actually called from the javascript code. It must be the case that these functions are the same, but somehow have different names?

The website is very simple - it contains an input field for a user to validate a candidate flag. The website loads a Javascript file `Y8splx37qY.js` which has the following contents:

```javascript
const _0x6d8f=['copy_char','value','207aLjBod','1301420SaUSqf','233ZRpipt','2224QffgXU','check_flag','408533hsoVYx','instance','278338GVFUrH','Correct!','549933ZVjkwI','innerHTML','charCodeAt','./aD8SvhyVkb','result','977AzKzwq','Incorrect!','exports','length','getElementById','1jIrMBu','input','615361geljRK'];const _0x5c00=function(_0x58505a,_0x4d6e6c){_0x58505a=_0x58505a-0xc3;let _0x6d8fc4=_0x6d8f[_0x58505a];return _0x6d8fc4;};(function(_0x12fd07,_0x4e9d05){const _0x4f7b75=_0x5c00;while(!![]){try{const _0x1bb902=-parseInt(_0x4f7b75(0xc8))*-parseInt(_0x4f7b75(0xc9))+-parseInt(_0x4f7b75(0xcd))+parseInt(_0x4f7b75(0xcf))+parseInt(_0x4f7b75(0xc3))+-parseInt(_0x4f7b75(0xc6))*parseInt(_0x4f7b75(0xd4))+parseInt(_0x4f7b75(0xcb))+-parseInt(_0x4f7b75(0xd9))*parseInt(_0x4f7b75(0xc7));if(_0x1bb902===_0x4e9d05)break;else _0x12fd07['push'](_0x12fd07['shift']());}catch(_0x4f8a){_0x12fd07['push'](_0x12fd07['shift']());}}}(_0x6d8f,0x4bb06));let exports;(async()=>{const _0x835967=_0x5c00;let _0x1adb5f=await fetch(_0x835967(0xd2)),_0x355961=await WebAssembly['instantiate'](await _0x1adb5f['arrayBuffer']()),_0x5c0ffa=_0x355961[_0x835967(0xcc)];exports=_0x5c0ffa[_0x835967(0xd6)];})();function onButtonPress(){const _0x50ea62=_0x5c00;let _0x5f4170=document[_0x50ea62(0xd8)](_0x50ea62(0xda))[_0x50ea62(0xc5)];for(let _0x19d3ca=0x0;_0x19d3ca<_0x5f4170['length'];_0x19d3ca++){exports[_0x50ea62(0xc4)](_0x5f4170[_0x50ea62(0xd1)](_0x19d3ca),_0x19d3ca);}exports['copy_char'](0x0,_0x5f4170[_0x50ea62(0xd7)]),exports[_0x50ea62(0xca)]()==0x1?document['getElementById'](_0x50ea62(0xd3))[_0x50ea62(0xd0)]=_0x50ea62(0xce):document[_0x50ea62(0xd8)](_0x50ea62(0xd3))['innerHTML']=_0x50ea62(0xd5);}
```

In this form, the javascript code is rather unsightly. I performed the following steps to improve its readability:
- Deobfuscated the code using https://obf-io.deobfuscate.io/
- Renamed variables appropriately
- Evaluated functions where possible. For instance `_0x50ea62(0xda)` evaluates to `"input"`

The resulting javascript code is:

- [ ] TODO: Finish this

```javascript
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
```

From this code, we can see that a web assembly binary called `aD8SvhyVkb` is being loaded. I first downloaded this file, saving it as `web_assembly.wasm`. Next, I converted the raw wasm binary to the Web Assembly Text (WAT) format using the [Web Assembly Binary Toolkit (WABT)](https://github.com/WebAssembly/wabt?tab=readme-ov-file). This makes the file slightly more human readable (although it is still difficult). I ran the command:

```
$ ~/tools/wabt/build/wasm2wat web_assembly.wasm -o web_assembly.wat
```

This produced the following contents in `web_assembly.wat`

```
(module
  (type $t0 (func))
  (type $t1 (func (param i32 i32) (result i32)))
  (type $t2 (func (result i32)))
  (type $t3 (func (param i32 i32)))
  (func $__wasm_call_ctors (export "__wasm_call_ctors") (type $t0))
  (func $strcmp (export "strcmp") (type $t1) (param $p0 i32) (param $p1 i32) (result i32)
    (local $l2 i32) (local $l3 i32) (local $l4 i32) (local $l5 i32) (local $l6 i32) (local $l7 i32) (local $l8 i32) (local $l9 i32) (local $l10 i32) (local $l11 i32) (local $l12 i32) (local $l13 i32) (local $l14 i32) (local $l15 i32) (local $l16 i32) (local $l17 i32) (local $l18 i32) (local $l19 i32) (local $l20 i32) (local $l21 i32) (local $l22 i32) (local $l23 i32) (local $l24 i32) (local $l25 i32) (local $l26 i32) (local $l27 i32) (local $l28 i32) (local $l29 i32) (local $l30 i32) (local $l31 i32) (local $l32 i32) (local $l33 i32) (local $l34 i32) (local $l35 i32) (local $l36 i32) (local $l37 i32) (local $l38 i32) (local $l39 i32) (local $l40 i32) (local $l41 i32) (local $l42 i32) (local $l43 i32)
    (local.set $l2
      (global.get $g0))
    (local.set $l3
      (i32.const 32))
    (local.set $l4
      (i32.sub
        (local.get $l2)
        (local.get $l3)))
    (i32.store offset=24
      (local.get $l4)
      (local.get $p0))
    (i32.store offset=20
      (local.get $l4)
      (local.get $p1))
    (local.set $l5
      (i32.load offset=24
        (local.get $l4)))
    (i32.store offset=16
      (local.get $l4)
      (local.get $l5))
    (local.set $l6
      (i32.load offset=20
        (local.get $l4)))
    (i32.store offset=12
      (local.get $l4)
      (local.get $l6))
    (block $B0
      (loop $L1
        (local.set $l7
          (i32.load offset=16
            (local.get $l4)))
        (local.set $l8
          (i32.const 1))
        (local.set $l9
          (i32.add
            (local.get $l7)
            (local.get $l8)))
        (i32.store offset=16
          (local.get $l4)
          (local.get $l9))
        (local.set $l10
          (i32.load8_u
            (local.get $l7)))
        (i32.store8 offset=11
          (local.get $l4)
          (local.get $l10))
        (local.set $l11
          (i32.load offset=12
            (local.get $l4)))
        (local.set $l12
          (i32.const 1))
        (local.set $l13
          (i32.add
            (local.get $l11)
            (local.get $l12)))
        (i32.store offset=12
          (local.get $l4)
          (local.get $l13))
        (local.set $l14
          (i32.load8_u
            (local.get $l11)))
        (i32.store8 offset=10
          (local.get $l4)
          (local.get $l14))
        (local.set $l15
          (i32.load8_u offset=11
            (local.get $l4)))
        (local.set $l16
          (i32.const 255))
        (local.set $l17
          (i32.and
            (local.get $l15)
            (local.get $l16)))
        (block $B2
          (br_if $B2
            (local.get $l17))
          (local.set $l18
            (i32.load8_u offset=11
              (local.get $l4)))
          (local.set $l19
            (i32.const 255))
          (local.set $l20
            (i32.and
              (local.get $l18)
              (local.get $l19)))
          (local.set $l21
            (i32.load8_u offset=10
              (local.get $l4)))
          (local.set $l22
            (i32.const 255))
          (local.set $l23
            (i32.and
              (local.get $l21)
              (local.get $l22)))
          (local.set $l24
            (i32.sub
              (local.get $l20)
              (local.get $l23)))
          (i32.store offset=28
            (local.get $l4)
            (local.get $l24))
          (br $B0))
        (local.set $l25
          (i32.load8_u offset=11
            (local.get $l4)))
        (local.set $l26
          (i32.const 255))
        (local.set $l27
          (i32.and
            (local.get $l25)
            (local.get $l26)))
        (local.set $l28
          (i32.load8_u offset=10
            (local.get $l4)))
        (local.set $l29
          (i32.const 255))
        (local.set $l30
          (i32.and
            (local.get $l28)
            (local.get $l29)))
        (local.set $l31
          (local.get $l27))
        (local.set $l32
          (local.get $l30))
        (local.set $l33
          (i32.eq
            (local.get $l31)
            (local.get $l32)))
        (local.set $l34
          (i32.const 1))
        (local.set $l35
          (i32.and
            (local.get $l33)
            (local.get $l34)))
        (br_if $L1
          (local.get $l35)))
      (local.set $l36
        (i32.load8_u offset=11
          (local.get $l4)))
      (local.set $l37
        (i32.const 255))
      (local.set $l38
        (i32.and
          (local.get $l36)
          (local.get $l37)))
      (local.set $l39
        (i32.load8_u offset=10
          (local.get $l4)))
      (local.set $l40
        (i32.const 255))
      (local.set $l41
        (i32.and
          (local.get $l39)
          (local.get $l40)))
      (local.set $l42
        (i32.sub
          (local.get $l38)
          (local.get $l41)))
      (i32.store offset=28
        (local.get $l4)
        (local.get $l42)))
    (local.set $l43
      (i32.load offset=28
        (local.get $l4)))
    (return
      (local.get $l43)))
  (func $check_flag (export "check_flag") (type $t2) (result i32)
    (local $l0 i32) (local $l1 i32) (local $l2 i32) (local $l3 i32) (local $l4 i32) (local $l5 i32) (local $l6 i32) (local $l7 i32) (local $l8 i32) (local $l9 i32) (local $l10 i32)
    (local.set $l0
      (i32.const 0))
    (local.set $l1
      (i32.const 1072))
    (local.set $l2
      (i32.const 1024))
    (local.set $l3
      (call $strcmp
        (local.get $l2)
        (local.get $l1)))
    (local.set $l4
      (local.get $l3))
    (local.set $l5
      (local.get $l0))
    (local.set $l6
      (i32.ne
        (local.get $l4)
        (local.get $l5)))
    (local.set $l7
      (i32.const -1))
    (local.set $l8
      (i32.xor
        (local.get $l6)
        (local.get $l7)))
    (local.set $l9
      (i32.const 1))
    (local.set $l10
      (i32.and
        (local.get $l8)
        (local.get $l9)))
    (return
      (local.get $l10)))
  (func $copy_char (export "copy_char") (type $t3) (param $p0 i32) (param $p1 i32)
    (local $l2 i32) (local $l3 i32) (local $l4 i32) (local $l5 i32) (local $l6 i32) (local $l7 i32) (local $l8 i32) (local $l9 i32) (local $l10 i32)
    (local.set $l2
      (global.get $g0))
    (local.set $l3
      (i32.const 16))
    (local.set $l4
      (i32.sub
        (local.get $l2)
        (local.get $l3)))
    (i32.store offset=12
      (local.get $l4)
      (local.get $p0))
    (i32.store offset=8
      (local.get $l4)
      (local.get $p1))
    (local.set $l5
      (i32.load offset=12
        (local.get $l4)))
    (block $B0
      (br_if $B0
        (i32.eqz
          (local.get $l5)))
      (local.set $l6
        (i32.load offset=12
          (local.get $l4)))
      (local.set $l7
        (i32.const 8))
      (local.set $l8
        (i32.xor
          (local.get $l6)
          (local.get $l7)))
      (i32.store offset=12
        (local.get $l4)
        (local.get $l8)))
    (local.set $l9
      (i32.load offset=12
        (local.get $l4)))
    (local.set $l10
      (i32.load offset=8
        (local.get $l4)))
    (i32.store8 offset=1072
      (local.get $l10)
      (local.get $l9))
    (return))
  (table $T0 1 1 funcref)
  (memory $memory (export "memory") 2)
  (global $g0 (mut i32) (i32.const 66864))
  (global $input (export "input") i32 (i32.const 1072))
  (global $__dso_handle (export "__dso_handle") i32 (i32.const 1024))
  (global $__data_end (export "__data_end") i32 (i32.const 1328))
  (global $__global_base (export "__global_base") i32 (i32.const 1024))
  (global $__heap_base (export "__heap_base") i32 (i32.const 66864))
  (global $__memory_base (export "__memory_base") i32 (i32.const 0))
  (global $__table_base (export "__table_base") i32 (i32.const 1))
  (data $d0 (i32.const 1024) "xakgK\5cNs9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00"))
```

Next I decided to decompile the output, attempting to produce something a little more understandable. To this end I ran the command:

```
~/tools/wabt/build/wasm-decompile web_assembly.wasm -o web_assembly.dcmp
```

This produced the following output:

```
export memory memory(initial: 2, max: 0);

global g_a:int = 66864;
export global input:int = 1072;
export global dso_handle:int = 1024;
export global data_end:int = 1328;
export global global_base:int = 1024;
export global heap_base:int = 66864;
export global memory_base:int = 0;
export global table_base:int = 1;

table T_a:funcref(min: 1, max: 1);

data d_xakgKNs989l1im8i890088k09nj9(offset: 1024) =
"xakgK\Ns9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00";

export function wasm_call_ctors() {
}

export function strcmp(a:int, b:int):int {
  var c:int = g_a;
  var d:int = 32;
  var e:int = c - d;
  e[6]:int = a;
  e[5]:int = b;
  var f:int = e[6]:int;
  e[4]:int = f;
  var g:int = e[5]:int;
  e[3]:int = g;
  loop L_b {
    var h:ubyte_ptr = e[4]:int;
    var i:int = 1;
    var j:int = h + i;
    e[4]:int = j;
    var k:int = h[0];
    e[11]:byte = k;
    var l:ubyte_ptr = e[3]:int;
    var m:int = 1;
    var n:int = l + m;
    e[3]:int = n;
    var o:int = l[0];
    e[10]:byte = o;
    var p:int = e[11]:ubyte;
    var q:int = 255;
    var r:int = p & q;
    if (r) goto B_c;
    var s:int = e[11]:ubyte;
    var t:int = 255;
    var u:int = s & t;
    var v:int = e[10]:ubyte;
    var w:int = 255;
    var x:int = v & w;
    var y:int = u - x;
    e[7]:int = y;
    goto B_a;
    label B_c:
    var z:int = e[11]:ubyte;
    var aa:int = 255;
    var ba:int = z & aa;
    var ca:int = e[10]:ubyte;
    var da:int = 255;
    var ea:int = ca & da;
    var fa:int = ba;
    var ga:int = ea;
    var ha:int = fa == ga;
    var ia:int = 1;
    var ja:int = ha & ia;
    if (ja) continue L_b;
  }
  var ka:int = e[11]:ubyte;
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = e[10]:ubyte;
  var oa:int = 255;
  var pa:int = na & oa;
  var qa:int = ma - pa;
  e[7]:int = qa;
  label B_a:
  var ra:int = e[7]:int;
  return ra;
}

export function check_flag():int {
  var a:int = 0;
  var b:int = 1072;
  var c:int = 1024;
  var d:int = strcmp(c, b);
  var e:int = d;
  var f:int = a;
  var g:int = e != f;
  var h:int = -1;
  var i:int = g ^ h;
  var j:int = 1;
  var k:int = i & j;
  return k;
}

function copy(a:int, b:int) {
  var c:int = g_a;
  var d:int = 16;
  var e:int_ptr = c - d;
  e[3] = a;
  e[2] = b;
  var f:int = e[3];
  if (eqz(f)) goto B_a;
  var g:int = e[3];
  var h:int = 8;
  var i:int = g ^ h;
  e[3] = i;
  label B_a:
  var j:int = e[3];
  var k:byte_ptr = e[2];
  k[1072] = j;
}
```

The above code defines three functions:
- `strcmp` takes in two memory offsets and compares the two strings at these offsets. Importantly it will return 0 if the two strings are the same.
- `check_flag` compares two strings at offsets 1024 and 1072. 1072 is the offset of the user input, and 1024 is the offset of `d_xakgKNs989l1im8i890088k09nj9`. If the two strings match, then the function returns 1, otherwise 0. Thus, it seems that the value of `d_xakgKNs989l1im8i890088k09nj9` contains the flag, however encoded in some capacity.
- `copy` is where the secret to the challenge is located. I will now explore this in more detail.

I will now go through the `copy` function line by line:
- The value assigned to `g_a` is stored in the variable `c`. `g_a` has the value 66864 (this value is defined as a global variable).
- The value 16 is stored in the variable `d`.
- A pointer variable is assigned that value `c - d` which in this case is 66864 - 16 = 66848. This is a memory location
- Recall that `e[3] = *(e+3)`. Thus we are writing the value of `a` to the byte offset 66851
- Similarly, we are writing the value `b` to the byte offset 66850
- Now we assign `e[3]` to `f`, but we know that `e[3]` contains the value of `a` i.e. `f` contains the value of `a`.
- The `eqz` function checks if a value is equal to 0. Thus `eqz(f)` checks if `f` is equal to 0. Recall that `f` contains the value of `a` so really this is what is being checked. If it is equal to 0, the program jumps to the label `B_a`.
- The value of `e[3]` is assigned to `g`. Again, since `e[3]` contains the value of `a`, so now does `g`.
- `h` is assigned the value of 8.
- `i` is assigned the result of the bitwise XOR operator applied to `g` and `h`. This essentially flips the first bit of `g`.
- The value of `i` is assigned to `e[3]`. This previously contained the value of `a`.
- The `label` indicates the point of the program where the prior equality check would resume execution.
- The value of `e[3]` is assigned to the variable `j`. Note that this is the value of `a` XORed with the value 8.
- The variable `k` is used to store the value in `e[2]`. Recall that `e[2]` holds the value of `b`.
- Finally, we have the line `k[1072] = j`. Remember that `k[1072] = *(k + 1072)`. Reordering the terms as `*(1072 + k)` gives this statement slightly more meaning. From the memory location 1072, we move `k` bytes along and write the value of `j`.

The above makes more sense when considered in the calling context. Consider the following snippet from the deobfuscated javascript code:

```javascript
  for (let i = 0; i < input_value.length; i++) {
    exports.copy_char(input_value.charCodeAt(i), i);
  }
```

This code iterates over the length of the input string, calling the `copy_char` function on each index. Assuming that `copy_char` is the same as the `copy` function in the web assembly, the value of `a` would be `input_value.charCodeAt(i)` or more simply, the character at index `i` in the input string. Similarly, the value of `b` is the index itself. We can infer the following from this understanding:
- `a` contains a character of the user input. This character is XORed with the value 8 before being stored.
- `b` contains the index of the character in `a` (the function does not require this, but the calling convention enforces it).
- The above `for` loop copies across the user input character by character into the web assembly memory, XORing each character with the value 8 while doing so. Importantly, the ordering of the characters is preserved.

We can now make sense of what the `check_flag` function is doing. Recall that it compares two strings at byte offsets 1024 and 1072. The string at byte offset 1024 is `"xakgK\Ns9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00"`. The string at byte offset 1072 is the user input, however it is the user input *after* being copied across into the web assembly memory. This means that each character has been XORed with 8 before being stored. Thus, if we reverse the XOR on the string at byte offset 1024, we should end up with the flag string. 

Using [Cyberchef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Decimal','string':'8'%7D,'Standard',false)&input=eGFrZ0tcTnM5PTg6OWwxP2ltOGk8ODk/MDA%2BODhrMDk9bmo5a2ltbnVcMDBcMDA) to do this produces the following result:

```
picoCTF{15021d97ae0a401788600c815fb1caef}T88T88
```

And thus the flag is:

```
picoCTF{15021d97ae0a401788600c815fb1caef}
```