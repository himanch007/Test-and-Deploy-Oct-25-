# Write your code below:
import surfshop
import unittest

class Tests(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test1_add_surf_board(self):
    m = self.cart.add_surfboards(1)
    self.assertEqual(m, 'Successfully added 1 surfboard to cart!')

  def test1_add_surf_board(self):
    print(self.cart.add_surfboards(5))

  def test2_add_surf_board(self):
    for i in range(2, 5):
      with self.subTest(i=i):
        m = self.cart.add_surfboards(i)
        self.assertEqual(m, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  #@unittest.skip
  def test3_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()
