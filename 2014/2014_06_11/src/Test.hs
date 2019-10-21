{-# LANGUAGE TemplateHaskell #-}
module Main (main) where

import Test.QuickCheck
import Test.Tasty (defaultMain, testGroup)
import Test.Tasty.QuickCheck (testProperty)
import Test.Tasty.TH
import Test.Tasty.HUnit
import HundredDoors

-- instance Arbitrary Xubiru where
--     arbitrary = elements [...]
--

prop_natural_add_is_always_positive n1 n2 = (n1 >= 0 && n2 >= 0) ==> add n1 n2 >= 0

--prop_sum_is_always_greater_or_equal_than_the_operands n1 n2 = (n1 >= 0 && n2 >= 0) ==> add n1 n2 >= 0

--
test_unit = [
        testGroup "Unit" [
            testCase "Case" (assertEqual "Add 1 2" (add 1 2) 3)
        ]
    ]

main :: IO ()
main = $defaultMainGenerator
