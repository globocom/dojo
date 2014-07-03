{-# LANGUAGE TemplateHaskell #-}
module Main (main) where

import Test.QuickCheck
import Test.Tasty (defaultMain, testGroup)
import Test.Tasty.QuickCheck (testProperty)
import Test.Tasty.TH
import Test.Tasty.HUnit
import Data.List
import ParentalTesting

instance Arbitrary BloodType where
  arbitrary = elements [A, B, AB, O]
--

-- prop_little_cat n1 n2 = (n1 >= 0 && n2 >= 0) ==> add n1 n2 >= 0

-- test_unit = [
--         testGroup "Unit" [
--             testCase "Case" (assertEqual "Add 1 2" (1 + 2) 3)
--         ]
--     ]

main :: IO ()
main = $defaultMainGenerator

prop_cross_commutative x y = cross x y == cross y x
prop_cross_persistence x = x `elem` cross x x
prop_cross_with_ab x y = (x == AB || y == AB) ==> not (O `elem` cross x y)
prop_cross_without_ab x y = (x /= AB && y /= AB) ==> O `elem` cross x y
prop_cross_with_a x y = (x == A || y == A) ==> A `elem` cross x y
prop_cross_with_b x y = (x == B || y == B) ==> B `elem` cross x y

test_unit = [
       testGroup "Unit" [
           testCase "Cross AB AB" (assertEqual "" (sort [AB, B, A]) (sort $ cross AB AB))
       ]
   ]
