import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.sikuli.android.ADBScreen;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Location;
import org.sikuli.script.Match;
import org.sikuli.script.Region;
import org.sikuli.script.Screen;
import org.sikuli.script.ScreenImage;

public class AndroidDemo {

	public static void main(String[] args) {
		try {
			System.out.println("Hello World");
			ADBScreen screen = new ADBScreen();
			Random ran = new Random();
			Region reg = new ADBScreen();
			ScreenImage image = screen.capture();
			for (int i = 0; i < 100; i++) {
				System.out.println(image.equals(screen.capture()));
				if (image.equals(screen.capture())) {

					int Rx = reg.exists(image).getX();
					int Ry = reg.exists(image).getY();
					int Rh = reg.exists(image).getH();
					int Rw = reg.exists(image).getW();
					int fx = Rx + ran.nextInt(Rw);
					int fy = Ry + ran.nextInt(Rh);
					Location Lr = new Location(fx, fy);
					performEvent(selectEvent(), screen, Lr);
				} else {
					image = screen.capture();
					i = i - 1;
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static String selectEvent() {

		List<String> eventList = new ArrayList<String>();
		eventList.add("click");
		// eventList.add("aboveClick");
		// eventList.add("belowClick");
		eventList.add("tap");
		eventList.add("swipeleft");
		eventList.add("swiperight");
		// eventList.add("aboveTap");
		// eventList.add("belowTap");
		// eventList.add("doubleClick");
		eventList.add("dragDrop");
		eventList.add("highlight");
		eventList.add("rightClick");
		eventList.add("mouseMove");
		eventList.add("swipeup");
		eventList.add("swipdown");
		return eventList.get(new Random().nextInt(eventList.size() - 0) + 0);
	}

	public static void performEvent(String eventToPerform, ADBScreen screen, Location Lr) {
		try {

			System.out.println("Event Selected" + eventToPerform);

			switch (eventToPerform) {
			case "click":
				screen.click();
				break;
			case "aboveClick":
				screen.above().click();

				break;
			case "belowClick":
				screen.below().click();
				break;

			case "tap":
				screen.aTap(Lr);
				break;
			case "aboveTap":
				screen.above().aTap(Lr);
				break;
			case "belowTap":
				screen.below().aTap(Lr);
				break;
			case "doubleClick":
				screen.doubleClick();
				break;
			case "dragDrop":
				screen.dragDrop(Lr);
				break;
			case "highlight":
				screen.highlight();
				break;
			case "rightClick":
				screen.rightClick();

				break;
			case "swipeleft":
				screen.aSwipeLeft();
				break;

			case "swiperight":
				screen.aSwipeRight();
				break;
			case "mouseMove":
				screen.mouseMove();

				break;
			case "swipeup":
				screen.aSwipeUp();

				break;
			case "swipedown":
				screen.aSwipeDown();

				break;

			default:
				break;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}
