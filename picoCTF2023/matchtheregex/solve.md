# picoCTF2023 MatchTheRegex Write Up

## Description

> How about trying to match a regular expression The website is running [here](http://saturn.picoctf.net:51596/).

## Solution

The website gives us an input field and a submit button. Attempting the input `test` produces an alert:

> wrong match! Try Again!

Given the challenge title, one would assume that the input is being checked against a regular expression, yielding the flag if the given input matches. Given the above result, one could also assume that `test` does not match the regex in question.

Looking at the page source code, there is an interesting function within a script tag at the end of the document:

```html
<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}

</script>
```

The function is called when the user presses the submit button. The function is making a GET request to `flag` endpoint with the users string as input. The request responds with a JSON object that is parsed and displayed to the user through an alert. The most interesting part of this function is the comment:

```
// ^p.....F!?
```

The syntax of this comment is indicative of a regular expression. In this particular case, the regular expression will match any string that is 8 characters long, starts with `p`  and ends with `F!`. Clearly the intended string is `picoCTF!`, however any string satisfying the above constraints will match the regular expression (e.g. `paaaaaF!`).

Submitting the string `picoCTF!` results in an alert containing the flag:

```
picoCTF{succ3ssfully_matchtheregex_9080e406}
```




