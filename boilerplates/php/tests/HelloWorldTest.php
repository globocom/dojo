<?php
    namespace Test;
    use App\HelloWorld;
    use PHPUnit\Framework\TestCase;
    class HelloWorldTest extends TestCase
    {
      public function testHelloWorld()
      {
       
        $hello_obj = new HelloWorld();

        $this->assertEquals("Hello World", $hello_obj->getHelloWorld());
      }
    }