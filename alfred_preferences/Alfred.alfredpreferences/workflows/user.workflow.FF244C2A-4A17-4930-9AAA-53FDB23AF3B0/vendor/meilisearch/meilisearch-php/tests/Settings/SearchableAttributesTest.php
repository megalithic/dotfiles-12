<?php

use MeiliSearch\Client;
use PHPUnit\Framework\TestCase;

define('__ROOT__', dirname(dirname(__FILE__)));
require_once __ROOT__.'/utils.php';

class SearchableAttributesTest extends TestCase
{
    private static $client;
    private static $index1;
    private static $index2;
    private static $primary_key;

    public static function setUpBeforeClass(): void
    {
        parent::setUpBeforeClass();
        static::$client = new Client('http://localhost:7700', 'masterKey');
        deleteAllIndexes(static::$client);
        static::$primary_key = 'objectID';
        static::$index1 = static::$client->createIndex('uid1');
        static::$index2 = static::$client->createIndex(['uid' => 'uid2', 'primaryKey' => static::$primary_key]);
    }

    public static function tearDownAfterClass(): void
    {
        parent::tearDownAfterClass();
        deleteAllIndexes(static::$client);
    }

    public function testGetDefaultSearchableAttributes()
    {
        $res = static::$index1->getSearchableAttributes();
        $this->assertIsArray($res);
        $this->assertEmpty($res);
        $res = static::$index2->getSearchableAttributes();
        $this->assertIsArray($res);
        $this->assertEquals([static::$primary_key], $res);
    }

    public function testUpdateSearchableAttributes()
    {
        $new_sa = [
            'title',
            'description',
        ];
        $res = static::$index1->updateSearchableAttributes($new_sa);
        $this->assertIsArray($res);
        $this->assertArrayHasKey('updateId', $res);
        usleep(10 * 1000);
        $sa = static::$index1->getSearchableAttributes();
        $this->assertIsArray($sa);
        $this->assertEquals($new_sa, $sa);
    }

    public function testResetSearchableAttributes()
    {
        $res = static::$index1->resetSearchableAttributes();
        $this->assertIsArray($res);
        $this->assertArrayHasKey('updateId', $res);
        usleep(10 * 1000);
        $sa = static::$index1->getSearchableAttributes();
        $this->assertIsArray($sa);
    }
}
