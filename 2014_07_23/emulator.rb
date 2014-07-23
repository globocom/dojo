class Operation

  attr_reader :name, :reg, :value, :address

  def initialize(instruction)
    if instruction & 0xf000 == 0x6000 
      @name = 'set'
      @reg = (0x0f00 & instruction) >> 8
      @value = 0x00ff & instruction
    elsif instruction == 0x0
      @name = 'end'
    elsif instruction & 0xf000 == 0x3000
      @name = 'skip'
      @reg = (0x0f00 & instruction) >> 8
      @value = 0x00ff & instruction
    elsif instruction & 0xf000 == 0x1000
      @name = 'jump'
      @address = 0x0fff & instruction
    elsif instruction & 0xf000 == 0x7000
      @name = 'increment'
      @reg = (0x0f00 & instruction) >> 8
      @value = 0x00ff & instruction
    end
  end
end

class Emulator

  attr_reader :registers, :pc

  def initialize
    @registers = [0] * 16
  end

  def exec(instructions)
    @pc = 0
    begin
      operation = Operation.new instructions[pc]
      if operation.name == 'set'
        registers[operation.reg] = operation.value
      elsif operation.name == 'skip'
        if registers[operation.reg] == operation.value
          @pc += 1
        end
      elsif operation.name == 'jump'
        @pc = operation.address - 1
      elsif operation.name == 'increment'
        registers[operation.reg] += operation.value
      end
      @pc += 1
    end while (operation.name != 'end')
  end
end
