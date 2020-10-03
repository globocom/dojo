class NumberToRoman
  ROMAN_LETTERS = {
    1    => "I",
    5    => "V",
    10   => "X",
    50   => "L",
    100  => "C",
    500  => "D",
    1000 => "M",
  }

  REPEAT_DICT = {
    "IIII" => "IV",
    "VIIII" => "IX",
    "XXXX" => "XL",
    "LXXXX" => "XC",
    "CCCC" => "CD",
    "DCCCC" => "CM"
  }

  def self.convert number
    roman = ""
    ROMAN_LETTERS.keys.reverse.each do |key|
      while number >= key
        roman += ROMAN_LETTERS[key]
        number -= key
      end
    end
    convert_four_repeated roman
  end

  def self.convert_four_repeated roman
    REPEAT_DICT.keys.reverse.each do |key|
      roman.gsub! key,REPEAT_DICT[key]
    end
    roman
  end
end
