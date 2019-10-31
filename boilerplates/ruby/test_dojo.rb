require_relative "dojo"
require "test/unit"
 
class TestDojo < Test::Unit::TestCase
 
  def test_true
    assert_true(Dojo.new().main(), "should return true")
  end
 
end