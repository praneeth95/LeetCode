/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if (word===word.toUpperCase()) {
            return true;
        }
        var len = word.length;
        for (var i = 1; i < word.length; i++) {
            var ch = word.charAt(i);
            if ('A' <= ch  && ch <= 'Z') { 					//[A-Z = 65-90]  and [a-z = 97-122] = leetcode, United
                return false;
            }
        }
        return true;
};