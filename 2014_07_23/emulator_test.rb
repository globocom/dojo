require 'spec_helper'

describe Emulator do
  before do
    @emu = Emulator.new
  end

  describe "init" do
    it "registers filled with zero" do
      @emu.registers.must_equal [0] * 16
    end
  end


  describe "execucao" do
    it "should set register" do
     @emu.exec([0x6177, 0x0000])
     @emu.registers.must_equal [0, 0x77] + [0]*14
    end

    it "program should finish on 0x0000" do
     @emu.exec([0x0000, 0x6177])
     @emu.registers.must_equal [0]*16
    end

    it "should skip 0x6277" do
     @emu.exec([0x3100, 0x6277, 0x6123, 0x0000])
     @emu.registers.must_equal [0, 0x23] + [0]*14
    end

    it "shouldn't skip 0x6277" do
     @emu.exec([0x3102, 0x6277, 0x6123, 0x0000])
     @emu.registers.must_equal [0, 0x23, 0x77] + [0]*13
    end

    it "should skip all instructions" do
     @emu.exec([0x1003, 0x6277, 0x6123, 0x6401, 0x0000])
     @emu.registers.must_equal [0, 0, 0, 0, 1] + [0]*11
    end

    it "should set v3 to 10" do
     @emu.exec([0x6101, 0x7109, 0x0000])
     @emu.registers.must_equal [0, 0x0a] + [0]*14
    end

    it "should set v3 to 10 with a loop" do
     @emu.exec([0x330a, 0x1003, 0x1005, 0x7301, 0x1000, 0x0000])
     @emu.registers.must_equal [0, 0, 0, 0x0a] + [0]*12
    end
  end
end
