import Transformer from '../../base/transformers/BaseTransformer'
import Campaign from '../models/Campaign'
import TokenTransformer from '@/tokens/transformers/TokenTransformer'
import getCurrencySymbol from '@/base/helpers/currencies'
import IncomeTransformer from './IncomeTransformer'
import RevenueTransformer from './RevenueTransformer'

class CampaignTransformer extends Transformer {
  static fetch (campaign) {
    return new Campaign({
      id: campaign.id,
      isDraft: campaign.is_draft,
      kind: campaign.kind,
      title: campaign.title,
      description: campaign.description,
      image: campaign.image,
      gender: campaign.gender,
      sport: campaign.sport,
      tags: campaign.tags,
      height: campaign.height,
      weight: campaign.weight,
      club: campaign.club,
      coach: campaign.coach,
      pitchUrl: campaign.pitch_url,
      pitchImage: campaign.pitch_image,
      ranking: campaign.ranking,
      biography: campaign.biography,
      achievements: campaign.achievements,
      expected: campaign.expected,
      currency: campaign.currency,
      currencySymbol: getCurrencySymbol(campaign.currency),
      funds: campaign.funds,
      softCap: campaign.soft_cap,
      use: campaign.use,
      giveBack: campaign.give_back,
      examples: campaign.examples,
      following: campaign.following,
      links: campaign.links,
      revenues: campaign.revenues.map(x => RevenueTransformer.fetch(x)),
      incomes: campaign.incomes.map(x => IncomeTransformer.fetch(x)),
      recommendations: campaign.recommendations,
      remaining: campaign.remaining,
      started: new Date(campaign.started),
      finished: new Date(campaign.finished),
      history: campaign.history,
      players: campaign.players,
      rating: campaign.rating,
      country: campaign.country,
      token: !!campaign.token ? TokenTransformer.fetch(campaign.token) : null,
    })
  }

  static send (campaign) {
    let data = {
      'id': campaign.id,
      'is_draft': campaign.isDraft,
      'kind': campaign.kind,
      'title': campaign.title,
      'description': campaign.description,
      'gender': campaign.gender,
      'sport': campaign.sport,
      'height': campaign.height,
      'weight': campaign.weight,
      'club': campaign.club,
      'coach': campaign.coach,
      'pitch_url': campaign.pitchUrl,
      'ranking': campaign.ranking,
      'biography': campaign.biography,
      'achievements': campaign.achievements,
      'expected': campaign.expected,
      'currency': campaign.currency,
      'funds': campaign.funds,
      'use': campaign.use,
      'give_back': campaign.giveBack,
      'examples': campaign.examples,
      'history': campaign.history,
      'players': campaign.players,
      'country': campaign.country,
    }
    if (!!campaign.tags) {
      data.tags = campaign.tags
    }
    return data
  }
}

export default CampaignTransformer
