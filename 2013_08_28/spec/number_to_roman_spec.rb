require_relative "../lib/number_to_roman"

describe NumberToRoman do
  context "simple numbers" do
    it "converts 1 to I" do
      expect(NumberToRoman.convert(1)).to eq("I")
    end

    it "converts 5 to V" do
      expect(NumberToRoman.convert(5)).to eq("V")
    end

    it "converts 10 to X" do
      expect(NumberToRoman.convert(10)).to eq("X")
    end

    it "converts 50 to L" do
      expect(NumberToRoman.convert(50)).to eq("L")
    end
  end

  context "repeated numbers" do
    it "converts 2 to II" do
      expect(NumberToRoman.convert(2)).to eq("II")
    end

    it "converts 20 to XX" do
      expect(NumberToRoman.convert(20)).to eq("XX")
    end
  end

  context "compound numbers" do
    it "converts 6 to VI" do
      expect(NumberToRoman.convert(6)).to eq("VI")
    end

    it "converts 22 to XXII" do
      expect(NumberToRoman.convert(22)).to eq("XXII")
    end
  end

  context "subtract numbers with prefix" do
    it "converts 24 to XXIV" do
      expect(NumberToRoman.convert(24)).to eq("XXIV")
    end

    it "converts 49 to XLIX" do
      expect(NumberToRoman.convert(49)).to eq("XLIX")
    end

    it "converts 99 to XCIX" do
      expect(NumberToRoman.convert(99)).to eq("XCIX")
    end
  end

  context "bob numbers" do
    it "convert 0 to a bob number" do
      expect(NumberToRoman.convert(0)).to eq("")
    end

    it "convert 888 to a LG number" do
      expect(NumberToRoman.convert(888)).to eq("DCCCLXXXVIII")
    end

    it "convert 1099 to another bob number" do
      expect(NumberToRoman.convert(1099)).to eq("MXCIX")
    end
  end
end
