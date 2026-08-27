package views.action;

import java.util.ArrayList;

import models.action.Action;
import models.action.Route;
import mvc.Observer;

import org.jsfml.graphics.Color;
import org.jsfml.graphics.FloatRect;
import org.jsfml.system.Vector2f;

import views.View;
import views.jsfml.VImage;
import views.jsfml.VTexte;

/**
 * Représentation graphique des listes d'Actions contenus dans la Route
 *
 */
public class VRouteListe extends View implements Observer {

	public static final int OFFSET = 35;

	private Route pRoute;
	private VTexte pVTexte;
	private VImage pFond;

	public VRouteListe(Route aRoute, FloatRect aZone) {
		super(aZone);
		this.pRoute = aRoute;
		this.pRoute.addObserver(this);
		this.pVTexte = null;
		initView();
	}

	public int findPosition(Vector2f aPosition) {
		int wDeplX = (int) aPosition.x / VRoute.LARGEUR;
		int wDplY = (int) (aPosition.y - OFFSET) / VRoute.HAUTEUR;
		return wDplY * 4 + wDeplX;
	}

	public Route getRoute() {
		return this.pRoute;
	}

	@Override
	public void initView() {
		VImage wImage_Fond = new VImage(new FloatRect(0, 0, getWidth(), getHeight()),
				"res/menu/cadreblanc.png");
		this.pFond = wImage_Fond;
		VTexte wVTexte = new VTexte(new FloatRect(0, 0, 0, 0), this.pRoute.getName() + "  ("
				+ this.pRoute.getTailleMax() + ")", OFFSET - 10);
		wVTexte.setColor(Color.BLACK);
		this.pVTexte = wVTexte;
		updateActions();
	}

	public void setTitreColor(Color aColor) {
		this.pVTexte.setColor(aColor);
	}

	@Override
	public void update(String aString, Object aObjet) {
		if (aString.equals("route_add")) {
			updateActions();
		}
		if (aString.equals("route_remove")) {
			updateActions();
		}
	}

	private void updateActions() {
		clearView();
		addView(this.pFond);
		addView(this.pVTexte);
		int wI = 0;
		int wX = 0;
		int wY = VRouteListe.OFFSET;
		ArrayList<Action> wActions = this.pRoute.getAction();
		for (Action wAction : wActions) {
			if (wI == 4) {
				wI = 0;
				wX = 0;
				wY = wY + VAction.HAUTEUR;
			}
			VAction wVAction = VAction.makeVAction(wAction, new FloatRect(wX, wY, VAction.LARGEUR,
					VAction.HAUTEUR));
			addView(wVAction);
			wX = wX + VAction.LARGEUR;
			wI++;
		}
	}
}
