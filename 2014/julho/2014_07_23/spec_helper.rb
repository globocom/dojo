require 'minitest/autorun'
require_relative 'emulator'

module MiniTest
  class Spec
    class << self
      alias_method :context, :describe
    end
  end
end
