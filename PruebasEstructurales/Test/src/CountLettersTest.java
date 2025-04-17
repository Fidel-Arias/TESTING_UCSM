import org.junit.jupiter.api.Test;

public class CountLettersTest {

    @Test
    public void testCount() {
        CountLetters countLetters = new CountLetters();
        int result = countLetters.count("Cars or car");
        assert result == 2 : "Expected 2, but got " + result;
    }
}
